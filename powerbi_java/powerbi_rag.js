//import powerbi from 'powerbi-client';
let loadedResolve;
let reportLoaded = new Promise((res) => { loadedResolve = res; });

let renderedResolve;
let reportRendered = new Promise((res) => { renderedResolve = res; });

const models = window.powerbi.models;

function embedPowerBIReport() {
    let accessToken = 'H4sIAAAAAAAEAB3Tx86jVgBA4Xf5t0SiGYMjzQJML9f0tqMX0y89yrtnJvuz-qTzz4-ZXN2Y5D9__9BE8jI6SEmOcU0NT9fsw_OwspLavJAIlafQK3BSF3PG3ZUnLzhY-iw4G5n8pxVCP2bGV2d8XxVANik0NauKbgjDWBF4x8Vjw7ndTeJ1QwyWMMrO2uDG0x2lG9D09WCmB0q_JUZkB2Q3UZbIX2s4EsDvZc1htnfHem-tBTy8uL12GOkg1Lw3x7fIzFVo4PTV6b5saRdAoYYWc82AiczEclSIA8Y9xTdaSXtiN4_GaOMlGpx7m7h9qUZ46TYac7OdB6j1rNMNCB2bR-YdClm8z-j0jmQMJd79Gb_gVcDBjIUWfN3vvh9jzPanBgCggWmhyiCnnIez7JzveH1CzzIeJB2SkfpYAn-PHJoUr00M1wEb0c80Hdmw5p-gXEmnj5BWzMxp9u6U_WYOhC8k6i9utawON2tz8ZvIMKzP_UaepEhfka5XRvoZqzq0FVC2AbRaWQP8uJ96puhGQiXjhjDmUYe9YSLFUW6EeN0WyreEatQJSKWCC_BcvYuk86Ih4CrxKzFmZo-p8LE4gqLlC5fdRjfrkFW8OTo-3GS-ZgUCPrSN520LrNQ8AAvWIf7kTkpS_S0eJhnA12KIOFWxmjv06Gk7-tchSW4UCStqn09hHs44g_fW7JdFlBdou4ed2VBPTRgU8upLawBQnDh1dO1Tn2Ool-Qio3rFk3XXPgDhMDHyrWzSrCkpRr7v0SQZGz9CR90HJ04AKxT8Eepb_U0IIbtjfrfM2721NXp-_PL41EANAnHTNd5zh9Zap2tIsymnNuPnr5_3ck3rqBXX7x3SYxgWQqU3oTNUtQkeSV1qRJarR_i4t4OMr6L_eg4zSATzhH3V-UyqkQWRDdy27V9TwEso53JFlag7-fA6si4n-rZMj8s4F1WCMVt8Dm-I148qebsx41nGhViDxOnuIkk8ewi_XUKJNULr2LSg3BfPEH2wOKO_Zk_yPOz0DatD_o2vmCZvt_53HWkulwrj-h7liGpcqNSnDI4yBr04pmyzihCgPFiYj5u-mwpRIwCSl5Rih_XeCu7p6_cp3IEPVyEV9qlY-u1NRKyiZ5PMRg_mDcWj0YX0wZMFC76-Gy1l2DWGuoewu9BZxdAmtHbuWAXktZRrs4jcsFiibdNsgBcmbf369Yf5mupiUfzfypzTjL2Q4FRT5Knd6Uddc9jxf-U01ZCs21L8zirmqT0X52GrzWQ3VLDmVhDYwaRw3aUwhqo4a0azUiDJK-GRQ2Rfp5LAmCYB3SMPOU6LV6DzzcdpgwTqkHcV3qEounRTdXjQmovjOZMhHp8pJSXUWD6zHf1SML7iU5TfaDz-YvZ3NftPvpCbtucj7M18jGpEJWTNoMKkhmik1I2rF-hHmjKsmdOw9KOOWBNnKFtgMTwb5DqJWqB12IsKAO9bgHVHoV7Eqdr3r0Gjz1ZgtOTEmJS3q_u1fUfCOiU-SD3jvUiC692EvEse7w2PjMR0qYOZej9nq8hiyRKe4-tlB6g6U1mgSyNJReSG6ZGpKXNlPJo6ZlZfREkQXpvdJjER_GH-9z8kvCTSAgYAAA==.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImV4cCI6MTczNjg2OTI5NywiYWxsb3dBY2Nlc3NPdmVyUHVibGljSW50ZXJuZXQiOnRydWV9'; // Replace with a valid token
    let embedUrl = 'https://app.powerbi.com/reportEmbed?reportId=dc20da54-0dde-4b7e-aa9c-4435bb7c71be&groupId=ceb0d1d0-6226-4aef-b245-fac7f89bb52e&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsidXNhZ2VNZXRyaWNzVk5leHQiOnRydWV9fQ%3d%3d';
    let config = {
        type: 'report',
        tokenType: 1,
        accessToken: accessToken,
        embedUrl: embedUrl,
        id: 'dc20da54-0dde-4b7e-aa9c-4435bb7c71be',
        permissions: 7,
        viewMode: 0,
        settings: {
            panes: {
                filters: { expanded: true, visible: true },
                pageNavigation: { visible: true },
            },
            bars: { statusBar: { visible: true } },
        }
    };

    const embedContainer = document.getElementById('report-container');
    const report = window.powerbi.embed(embedContainer, config);

    report.on("loaded", function () {
        loadedResolve();
    });

    report.on("rendered", function () {
        renderedResolve();
    });

    report.on("error", function (event) {
        console.error("Power BI Report Error:", event.detail);
    });

    return report;
}

async function loadAndEditReport() {
    let report = embedPowerBIReport();

    await reportLoaded;
    console.log("Report loaded successfully.");

    await reportRendered;
    console.log("Report rendered successfully.");

    await extractVisualData(report);
}
/**
async function extractVisualData(report) {
    let pages = await report.getPages();
    for (let page of pages) {
        try {
            let visuals = await page.getVisuals();
            for (let visual of visuals) {
                console.log(`Extracting data from visual: ${visual.name}`);
                let result = await visual.exportData(0);

                // Check if result.data is a string
                if (typeof result.data === "string") {
                    // Save the string directly as a CSV
                    downloadCSV(result.data, `${visual.name}.csv`);
                } else {
                    console.warn(`Unexpected data format for visual ${visual.name}:`, result.data);
                }
            }
        } catch (error) {
            console.error("Error extracting visual data:", error);
        }
    }
}

function downloadCSV(content, filename) {
    const blob = new Blob([content], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}


**/

async function extractVisualData(report) {

let pages = await report.getPages();
for (let page of pages) {

    try {
        let visuals = await page.getVisuals();
        for (let visual of visuals) {
            console.log(`Extracting data from visual: ${visual.name}`);
            let result = await visual.exportData(0);
            console.log(`Data for visual ${visual.name}:`, result.data);
        }
        
    } catch (error) {
        console.error("Error extracting visual data:", error);
    }
}
}

// Load the report when the page is ready
$(document).ready(loadAndEditReport);
