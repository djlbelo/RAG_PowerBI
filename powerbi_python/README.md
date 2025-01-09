# Power BI Data Retrieval and Summary

This project retrieves and summarizes data from Power BI using the Power BI REST API. It includes functionalities to fetch datasets, reports, dashboards, groups, users, and tiles, and then summarizes this information into a JSON file.

## Prerequisites

- Python 3.x
- `requests` library
- `msal` library

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required libraries:
    ```sh
    pip install requests msal
    ```

3. Update the key by the hardcoded mode and display the link in a box:
    ```python
    #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports-in-group#code-try-0
    access_token = 'eyJ0eXAiOi...'
    ```

## Configuration

Update the following constants in `rag_power_bi.py` with your Power BI and Azure AD details:
- `TENANT_ID`
- `CLIENT_ID`
- `CLIENT_SECRET`
- `GROUP_ID`

## Usage

Run the main script to retrieve and summarize the Power BI data:
```sh
python rag_power_bi.py