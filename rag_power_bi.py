import json
import requests
import msal

from credentials import username, password

# Constants
TENANT_ID = '057866cb-0e0f-4818-bd4a-0255845df359'
CLIENT_ID = '7fc05981-ef3e-4198-beed-6559a6a4c443'
CLIENT_SECRET = 'Tld8Q~hX_c4u8oYJfrdVd3KeZDvVVcpesAFywdce'
AUTHORITY_URL = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
GROUP_ID = 'ceb0d1d0-6226-4aef-b245-fac7f89bb52e'
POWER_BI_API_URL = f'https://api.powerbi.com/v1.0/myorg/groups/{GROUP_ID}/'

# Variables
access_token = ''

# Authenticate and get access token
if not access_token:
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY_URL,
        client_credential=CLIENT_SECRET
    )
    result = app.acquire_token_for_client(scopes=SCOPE)
    if 'access_token' in result:
        access_token = result['access_token']
    else:
        print('Could not obtain access token, trying acquiring token by username and password')
        result = app.acquire_token_by_username_password(
            username,
            password,
            scopes=SCOPE
        )
        if 'access_token' in result:
            access_token = result['access_token']
        else:
            raise Exception('Could not obtain access token both ways')

# Hardcoded access token https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports-in-group#code-try-0
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMDU3ODY2Y2ItMGUwZi00ODE4LWJkNGEtMDI1NTg0NWRmMzU5LyIsImlhdCI6MTczMzgyNjUyOSwibmJmIjoxNzMzODI2NTI5LCJleHAiOjE3MzM4MzIwOTAsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84WUFBQUErOGVEeEV5MTBpMHcxaFBDa3ZzWDNIenRISFdCcE1TdHc2L29FeGZibWFLMTFOTWcyWnRjTlFxZHJmUTYxdVBzeWNrMThWVDVzWFIzZExBRFlpT0NaLzZtOTJkZjM5LzZ0T1FmL0t6ZGFiZz0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJCZWxvIiwiZ2l2ZW5fbmFtZSI6IkR1YXJ0ZSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE5NS4yMy43Mi4xNSIsIm5hbWUiOiJEdWFydGUgQmVsbyIsIm9pZCI6IjUwMGI3NTU4LTA2OTgtNDFkMi1hMDBmLTI3ZjdlMmZiOTFhOCIsInB1aWQiOiIxMDAzMjAwM0M4MzIyRkQ3IiwicmgiOiIxLkFWNEF5Mlo0QlE4T0dFaTlTZ0pWaEYzeldRa0FBQUFBQUFBQXdBQUFBQUFBQUFBUkFibGVBQS4iLCJzY3AiOiJBcHAuUmVhZC5BbGwgQ2FwYWNpdHkuUmVhZC5BbGwgQ2FwYWNpdHkuUmVhZFdyaXRlLkFsbCBDb25uZWN0aW9uLlJlYWQuQWxsIENvbm5lY3Rpb24uUmVhZFdyaXRlLkFsbCBDb250ZW50LkNyZWF0ZSBEYXNoYm9hcmQuUmVhZC5BbGwgRGFzaGJvYXJkLlJlYWRXcml0ZS5BbGwgRGF0YWZsb3cuUmVhZC5BbGwgRGF0YWZsb3cuUmVhZFdyaXRlLkFsbCBEYXRhc2V0LlJlYWQuQWxsIERhdGFzZXQuUmVhZFdyaXRlLkFsbCBHYXRld2F5LlJlYWQuQWxsIEdhdGV3YXkuUmVhZFdyaXRlLkFsbCBJdGVtLkV4ZWN1dGUuQWxsIEl0ZW0uRXh0ZXJuYWxEYXRhU2hhcmUuQWxsIEl0ZW0uUmVhZFdyaXRlLkFsbCBJdGVtLlJlc2hhcmUuQWxsIE9uZUxha2UuUmVhZC5BbGwgT25lTGFrZS5SZWFkV3JpdGUuQWxsIFBpcGVsaW5lLkRlcGxveSBQaXBlbGluZS5SZWFkLkFsbCBQaXBlbGluZS5SZWFkV3JpdGUuQWxsIFJlcG9ydC5SZWFkV3JpdGUuQWxsIFJlcHJ0LlJlYWQuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWQuQWxsIFN0b3JhZ2VBY2NvdW50LlJlYWRXcml0ZS5BbGwgVGVuYW50LlJlYWQuQWxsIFRlbmFudC5SZWFkV3JpdGUuQWxsIFVzZXJTdGF0ZS5SZWFkV3JpdGUuQWxsIFdvcmtzcGFjZS5HaXRDb21taXQuQWxsIFdvcmtzcGFjZS5HaXRVcGRhdGUuQWxsIFdvcmtzcGFjZS5SZWFkLkFsbCBXb3Jrc3BhY2UuUmVhZFdyaXRlLkFsbCIsInN1YiI6IklTRlJnUmJ6aUpfZDdhM2VnX2hiMFNtSVh5NzIwY0tWYl9CRjAxWHlIRkkiLCJ0aWQiOiIwNTc4NjZjYi0wZTBmLTQ4MTgtYmQ0YS0wMjU1ODQ1ZGYzNTkiLCJ1bmlxdWVfbmFtZSI6ImR1YXJ0ZS5iZWxvQGNsb3Nlci5wdCIsInVwbiI6ImR1YXJ0ZS5iZWxvQGNsb3Nlci5wdCIsInV0aSI6IkZiZjFINWl5STA2eVpoaWFnWVYzQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfaWRyZWwiOiIxIDIyIn0.kwMNLJeLYoyeNL_nwou37d1CiVjmIlWeHQUp7SGTMbBMuU-rm7Wh3hwrkyvQ2-wabawK6STeOubJ5G6j2LeVJtz8aY5aaaKMF7863AnMzLjaFUDLl6qhIIW42UDDtcu_58Lov56FPU9khoTbwMMcDH-d51bxd-ZoTfVK99mf2LBwKsAZocaeI7q5CtEQXvZZ0xOFaS3nBOA_jbGp1dUNLY8yb0wJ0cUXwwS73B5CpwbFKg03uUoEUUUtSpCjT6F8m0b-C3t7AF7AIjk6e_NNHQuLC5AgAOt78-8rTGbWAdh7WNPtEbh1fWegjrOd0OZvD4Vy5FBXbt5lktgwO6-w8w'
headers = {'Authorization': f'Bearer {access_token}'}

# Retrieve datasets
def get_datasets():
    response = requests.get(f'{POWER_BI_API_URL}datasets', headers=headers)
    if response.status_code == 200:
        # create a json file with the datasets in responses folder
        with open('responses/datasets.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    print(f'Error retrieving datasets: {response}')

# Retrieve reports
def get_reports():
    response = requests.get(f'{POWER_BI_API_URL}reports', headers=headers)
    if response.status_code == 200:
        # create a json file with the reports in responses folder
        with open('responses/reports.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    print(f'Error retrieving reports: {response}')



# Retrieve dashboards
def get_dashboards():
    response = requests.get(f'{POWER_BI_API_URL}dashboards', headers=headers)
    if response.status_code == 200:
        # create a json file with the dashboards in responses folder
        with open('responses/dashboards.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    print(f'Error retrieving dashboards: {response}')# Retrieve groups

def get_tiles(dashboard):
    dashboard_name = dashboard['displayName']
    dashboard_id = dashboard['id']
    #get dashboard tiles
    response = requests.get(f'{POWER_BI_API_URL}dashboards/{dashboard_id}/tiles', headers=headers)
    if response.status_code == 200:
        # TO-DO: create a json file with the dashboard tiles in responses folder
        with open(f'responses/tiles/tiles_{dashboard_name}.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
    else:
        print(f'Error retrieving dashboard tiles: {response}')

def get_groups():
    response = requests.get(f'{POWER_BI_API_URL}groups', headers=headers)
    if response.status_code == 200:
        # create a json file with the groups in responses folder
        with open('responses/groups.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print(f'Error retrieving groups: {response}')# Retrieve users

def get_users():
    response = requests.get(f'{POWER_BI_API_URL}users', headers=headers)
    if response.status_code == 200:
        # create a json file with the users in responses folder
        with open('responses/users.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
        return response.json()
    else:
        print(f'Error retrieving users: {response}')


# Summarize information
def summarize_info():
    datasets = get_datasets()
    reports = get_reports()
    dashboards = get_dashboards()
    groups = get_groups()
    users = get_users()

    #dictionary of tiles for each dashboard
    tiles = {}
    for dashboard in dashboards['value']:
        tiles[dashboard['displayName']] = get_tiles(dashboard)

    summary = {
        'total_datasets': [dataset['name'] for dataset in datasets['value']] if datasets and 'value' in datasets else [],
        'total_reports': {report['name']: report['id'] for report in reports['value']} if reports and 'value' in reports else {},
        'total_dashboards': [dashboard['displayName'] for dashboard in dashboards['value']] if dashboards and 'value' in dashboards else [],
        'total_groups': [group['name'] for group in groups['value']] if groups and 'value' in groups else [],
        'total_users': [user['displayName'] for user in users['value']] if users and 'value' in users else [],
        'total_tiles': tiles
    }
    return summary

# Main function
def main():
    if access_token:
        print(f'Access token obtained successfully\n + {access_token}\n')
        summary = summarize_info()
        with open('responses/summary.json', 'w') as f:
            f.write(json.dumps(summary, indent=4))

        i = 0
        # Get each report
        keys = list(summary['total_reports'].keys())
        for report_id in summary['total_reports'].values():
            response = requests.get(f'{POWER_BI_API_URL}reports/{report_id}', headers=headers)
            if response.status_code == 200:
                with open(f'responses/reports/{keys[i]}.json', 'w') as f:
                    f.write(json.dumps(response.json(), indent=4))
                i += 1
            else:
                print(f'Error retrieving report {report_id}: {response}')
        print(f'Summary: {summary}')



if __name__ == '__main__':
    main()