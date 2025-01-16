
const getAccessToken = async function () {
    // Create a config variable that store credentials from config.json
    const config = require('./config/config.json');

    // Use MSAL.js for authentication
    const msal = require("@azure/msal-node");

    const msalConfig = {
        auth: {
            clientId: config.clientId,
            authority: `${config.authorityUrl}${config.tenantId}`,
        }
    };

    // Check for the MasterUser Authentication
    if (config.authenticationMode.toLowerCase() === "masteruser") {
        const clientApplication = new msal.PublicClientApplication(msalConfig);

        const usernamePasswordRequest = {
            scopes: [config.scopeBase],
            username: config.pbiUsername,
            password: config.pbiPassword
        };

        return clientApplication.acquireTokenByUsernamePassword(usernamePasswordRequest);

    };

    // Service Principal auth is the recommended by Microsoft to achieve App Owns Data Power BI embedding
    if (config.authenticationMode.toLowerCase() === "serviceprincipal") {
        msalConfig.auth.clientSecret =  config.clientSecret
        const clientApplication = new msal.ConfidentialClientApplication(msalConfig);

        const clientCredentialRequest = {
            scopes: [config.scopeBase],
        };

        return clientApplication.acquireTokenByClientCredential(clientCredentialRequest);
    }
}

module.exports.getAccessToken = getAccessToken;


async function getData(url) {
    try {
        const response = await axios.get(url, {
            headers: { 'Authorization': `Bearer ${accessToken}` }
        });
        return response.data;
    } catch (error) {
        console.log(`Error retrieving data: ${error}`);
    }
}

async function getDatasets() {
    const datasets = await getData(`${POWER_BI_API_URL}datasets`);
    if (datasets) {
        fs.writeFileSync('responses/datasets.json', JSON.stringify(datasets, null, 4));
    }
    return datasets;
}

async function getReports(groupId) {
    const reports = await getData(`${POWER_BI_API_URL}/groups/${groupId}/reports`);
    if (reports) {
        fs.writeFileSync('responses/reports.json', JSON.stringify(reports, null, 4));
    }
    return reports;
}

async function getDashboards(groupId) {
    const dashboards = await getData(`${POWER_BI_API_URL}/groups/${groupId}/dashboards`);
    if (dashboards) {
        fs.writeFileSync('responses/dashboards.json', JSON.stringify(dashboards, null, 4));
    }
    return dashboards;
}

async function getGroups() {
    const groups = await getData(`${POWER_BI_API_URL}groups`);
    if (groups) {
        fs.writeFileSync('responses/groups.json', JSON.stringify(groups, null, 4));
    }
    return groups;
}

async function getUsers(groupId) {
    const users = await getData(`${POWER_BI_API_URL}/groups/${groupId}/users`);
    if (users) {
        fs.writeFileSync('responses/users.json', JSON.stringify(users, null, 4));
    }
    return users;
}

async function getPages(groupId, reportId) {
    const pages = await getData(`${POWER_BI_API_URL}/groups/${groupId}/reports/${reportId}/pages`);
    if (pages) {
        fs.writeFileSync(`responses/pages_${reportId}.json`, JSON.stringify(pages, null, 4));
    }
    return pages;
}

async function getEmbedToken(groupId, reportId) {
    const requestBody = {
        accessLevel: 'View',
        allowSaveAs: true
    };
    try {
        const response = await axios.post(`${POWER_BI_API_URL}/groups/${groupId}/reports/${reportId}/GenerateToken`, requestBody, {
            headers: {
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json'
            }
        });
        if (response.data) {
            fs.writeFileSync(`responses/embed_token_${reportId}.json`, JSON.stringify(response.data, null, 4));
        }
        return response.data.token;
    } catch (error) {
        console.log(`Error retrieving embed token: ${error}`);
    }
}

async function summarizeInfo() {
    const summary = {};
    const groups = await getGroups();
    for (const group of groups.value) {
        const groupId = group.id;
        summary[groupId] = {};
        const reports = await getReports(groupId);
        for (const report of reports.value) {
            summary[groupId][report.id] = {
                name: report.name,
                pages: await getPages(GROUP_ID, report.id).value,
                embed_token: await getEmbedToken(GROUP_ID, report.id),
                embed_url: report.embedUrl,
                dataset_id: report.datasetId,
                csv_files: []
            };
        }
    }
    fs.writeFileSync('./summary.json', JSON.stringify(summary, null, 4));
    return summary;
}

(async () => {
    await summarizeInfo();
})();