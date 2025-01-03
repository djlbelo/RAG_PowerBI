from io import StringIO
import msal
import pandas as pd
import requests
from powerbiclient import Report
from flask import Flask, render_template

# Use the correct scope for Power BI APIs
SCOPE = ["https://analysis.windows.net/powerbi/api/.default"]
# URL for your tenant
AUTHORITY_URL = "https://login.microsoftonline.com/{tenant_id}"


def authenticate_with_msal(client_id, tenant_id):
    """Authenticate using MSAL with interactive login and return an access token."""
    try:
        # Create an MSAL PublicClientApplication instance for user authentication
        app = msal.PublicClientApplication(
            client_id,
            authority=AUTHORITY_URL.format(tenant_id=tenant_id)
        )

        # Attempt to acquire the token interactively
        result = app.acquire_token_interactive(scopes=SCOPE)
        print(result)

        # Check if the token was successfully acquired
        if "access_token" in result:
            print("Authentication successful.")
            return result["access_token"]
        else:
            print(f"Error obtaining access token: {result}")
            return None
    except Exception as e:
        print(f"Authentication error: {e}")
        return None


def generate_embed_token(access_token, group_id, report_id):
    """Generate an embed token for the Power BI report."""
    try:
        url = f"https://api.powerbi.com/v1.0/myorg/groups/{
        group_id}/reports/{report_id}/GenerateToken"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        body = {
            "accessLevel": "View"
        }

        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            embed_token = response.json().get("token")
            print("Embed token generated successfully.")
            return embed_token
        else:
            print(f"Failed to generate embed token: {
            response.status_code} {response.text}")
            return None
    except Exception as e:
        print(f"Error generating embed token: {e}")
        return None


def embed_report(report_id, group_id, embed_url, embed_token):
    """Embed the Power BI report using the provided URL and token."""
    try:
        report = Report(
            report_id=report_id,
            group_id=group_id,
            embed_url=embed_url,
            embed_token=embed_token
        )
        print("Report embedded successfully.")
        return report
    except Exception as e:
        print(f"Error embedding report: {e}")
        return None


def summarize_vis_info(report: Report):
    # Define the types of visuals to export data for
    visual_types_to_export = ['barChart', 'lineChart', 'pieChart', 'clusteredColumnChart', 'table', 'tableEx', 'map',
                              'slicer', 'lineClusteredColumnComboChart', 'shapeMap', 'decompositionTreeVisual', 'card']

    # Iterate over the visuals and export data for the specified types
    for page in report.get_pages():
        page_name = page['name']
        report.set_active_page(page_name)
        page_display_name = page['displayName']
        visuals = report.visuals_on_page(page_name)
        for visual in visuals:
            if visual['type'] in visual_types_to_export:
                try:
                    summarized_exported_data = report.export_visual_data(
                        page_name, visual['name'], rows=20)
                    data = StringIO(summarized_exported_data)
                    # Load data into pandas DataFrame
                    df = pd.read_csv(data, sep=",")
                    # Store the DataFrame as a CSV file in the 'csv' folder
                    csv_file_path = f'csv/{visual["type"]}_{visual["title"].replace(
                        " ", "_")}_{visual['name']}_{page_display_name.replace(" ", "_")}.csv'
                    df.to_csv(csv_file_path, index=False)
                    print(
                        f"Data for visual '{visual["title"].replace(" ", "")}' of type '{visual['type']}' exported successfully.")
                except Exception as e:
                    print(
                        f"Could not export data for visual '{visual["title"].replace(" ", "")}' of type '{visual['type']}': {e}")
        page['isActive'] = False


app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page with the embedded report."""
    return render_template('index.html', iframe=EMBED_URL)


if __name__ == "__main__":
    # Replace these placeholders with your configuration
    CLIENT_ID = '04bb970d-3099-4845-b81d-92e23362f261'
    TENANT_ID = '057866cb-0e0f-4818-bd4a-0255845df359'
    GROUP_ID = 'ceb0d1d0-6226-4aef-b245-fac7f89bb52e'
    EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=dc20da54-0dde-4b7e-aa9c-4435bb7c71be&autoAuth=true&ctid=057866cb-0e0f-4818-bd4a-0255845df359"
    REPORT_ID = "dc20da54-0dde-4b7e-aa9c-4435bb7c71be"

    app.run(debug=True)

    # Step 1: Authenticate (interactive flow)
    access_token = authenticate_with_msal(CLIENT_ID, TENANT_ID)

    if access_token:
        # Step 2: Generate Embed Token
        embed_token = generate_embed_token(access_token, GROUP_ID, REPORT_ID)

        if embed_token:
            # Step 3: Embed the Report
            print(embed_token)
            #
            report = embed_report(REPORT_ID, GROUP_ID, EMBED_URL, embed_token)
            # print(report._get_embed_state())
            if report:
                print("Power BI report embedding complete.")
                # Call the summarize_vis_info function with the report object

                report.on(event="loaded",
                          callback=lambda: print("Report loaded"))
                report.on(event='rendered',
                          callback=lambda: print("Report rendered"))

                with app.app_context():
                    summarize_vis_info(report)
            else:
                print("Failed to embed the report.")
        else:
            print("Embed token generation failed.")
    else:
        print("Authentication failed. Exiting.")