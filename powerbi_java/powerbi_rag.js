//import powerbi from 'powerbi-client';
let loadedResolve;
let reportLoaded = new Promise((res) => { loadedResolve = res; });

let renderedResolve;
let reportRendered = new Promise((res) => { renderedResolve = res; });

const visualTypesToExport = [
    'barChart', 'lineChart', 'pieChart', 'clusteredColumnChart', 'table', 'tableEx', 'map', 'slicer',
    'lineClusteredColumnComboChart', 'shapeMap', 'decompositionTreeVisual', 'card'
];

let accessToken = 'H4sIAAAAAAAEAB3Tx86jVgBA4Xf5t0SiGYMjzQJML9f0tqMX0y89yrtnJvuz-qTzz4-ZXN2Y5D9__9BE8jI6SEmOcU0NT9fsw_OwspLavJAIlafQK3BSF3PG3ZUnLzhY-iw4G5n8pxVCP2bGV2d8XxVANik0NauKbgjDWBF4x8Vjw7ndTeJ1QwyWMMrO2uDG0x2lG9D09WCmB0q_JUZkB2Q3UZbIX2s4EsDvZc1htnfHem-tBTy8uL12GOkg1Lw3x7fIzFVo4PTV6b5saRdAoYYWc82AiczEclSIA8Y9xTdaSXtiN4_GaOMlGpx7m7h9qUZ46TYac7OdB6j1rNMNCB2bR-YdClm8z-j0jmQMJd79Gb_gVcDBjIUWfN3vvh9jzPanBgCggWmhyiCnnIez7JzveH1CzzIeJB2SkfpYAn-PHJoUr00M1wEb0c80Hdmw5p-gXEmnj5BWzMxp9u6U_WYOhC8k6i9utawON2tz8ZvIMKzP_UaepEhfka5XRvoZqzq0FVC2AbRaWQP8uJ96puhGQiXjhjDmUYe9YSLFUW6EeN0WyreEatQJSKWCC_BcvYuk86Ih4CrxKzFmZo-p8LE4gqLlC5fdRjfrkFW8OTo-3GS-ZgUCPrSN520LrNQ8AAvWIf7kTkpS_S0eJhnA12KIOFWxmjv06Gk7-tchSW4UCStqn09hHs44g_fW7JdFlBdou4ed2VBPTRgU8upLawBQnDh1dO1Tn2Ool-Qio3rFk3XXPgDhMDHyrWzSrCkpRr7v0SQZGz9CR90HJ04AKxT8Eepb_U0IIbtjfrfM2721NXp-_PL41EANAnHTNd5zh9Zap2tIsymnNuPnr5_3ck3rqBXX7x3SYxgWQqU3oTNUtQkeSV1qRJarR_i4t4OMr6L_eg4zSATzhH3V-UyqkQWRDdy27V9TwEso53JFlag7-fA6si4n-rZMj8s4F1WCMVt8Dm-I148qebsx41nGhViDxOnuIkk8ewi_XUKJNULr2LSg3BfPEH2wOKO_Zk_yPOz0DatD_o2vmCZvt_53HWkulwrj-h7liGpcqNSnDI4yBr04pmyzihCgPFiYj5u-mwpRIwCSl5Rih_XeCu7p6_cp3IEPVyEV9qlY-u1NRKyiZ5PMRg_mDcWj0YX0wZMFC76-Gy1l2DWGuoewu9BZxdAmtHbuWAXktZRrs4jcsFiibdNsgBcmbf369Yf5mupiUfzfypzTjL2Q4FRT5Knd6Uddc9jxf-U01ZCs21L8zirmqT0X52GrzWQ3VLDmVhDYwaRw3aUwhqo4a0azUiDJK-GRQ2Rfp5LAmCYB3SMPOU6LV6DzzcdpgwTqkHcV3qEounRTdXjQmovjOZMhHp8pJSXUWD6zHf1SML7iU5TfaDz-YvZ3NftPvpCbtucj7M18jGpEJWTNoMKkhmik1I2rF-hHmjKsmdOw9KOOWBNnKFtgMTwb5DqJWqB12IsKAO9bgHVHoV7Eqdr3r0Gjz1ZgtOTEmJS3q_u1fUfCOiU-SD3jvUiC692EvEse7w2PjMR0qYOZej9nq8hiyRKe4-tlB6g6U1mgSyNJReSG6ZGpKXNlPJo6ZlZfREkQXpvdJjER_GH-9z8kvCTSAgYAAA==.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImV4cCI6MTczNjg2OTI5NywiYWxsb3dBY2Nlc3NPdmVyUHVibGljSW50ZXJuZXQiOnRydWV9'; // Replace with a valid token
let embedUrl = 'https://app.powerbi.com/reportEmbed?reportId=dc20da54-0dde-4b7e-aa9c-4435bb7c71be&groupId=ceb0d1d0-6226-4aef-b245-fac7f89bb52e&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsidXNhZ2VNZXRyaWNzVk5leHQiOnRydWV9fQ%3d%3d';

/**
 * Embeds a Power BI report into the specified container.
 * @param {string} embedUrl - The URL of the Power BI report to embed.
 * @param {string} accessToken - The access token for authenticating the Power BI report.
 * @returns {object} The embedded Power BI report object.
 */
function embedPowerBIReport(embedUrl, accessToken) {
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

async function loadAndEditReport(embedUrl, accessToken) {
    let report = embedPowerBIReport(embedUrl, accessToken);

    await reportLoaded;
    console.log("Report loaded successfully.");

    await reportRendered;
    console.log("Report rendered successfully.");

    await extractVisualData(report);
}

//TODO: Call from  metadata storage
const info = {
    "ceb0d1d0-6226-4aef-b245-fac7f89bb52e": {
        "dc20da54-0dde-4b7e-aa9c-4435bb7c71be": {
            "name": "US Sales Analysis",
            "pages": [
                {
                    "name": "ReportSectiondecccb8482fa6cf4f797",
                    "displayName": "Regional Sales Analysis",
                    "order": 0
                },
                {
                    "name": "ReportSection98ceb79bc32f027d9868",
                    "displayName": "Page tooltip",
                    "order": 1
                }
            ],
            "embed_token": "H4sIAAAAAAAEACXTR6uEZgCF4f9ytwbUsQeysPfxszvu7L230ZD_nhuyf-HAA-fvH5Dc_ZTkP3_-aIKJ3KZHK8N4mPADzTwAyAxqH_uGZCNTrSKu7_Pht7o6RX5k8ePz8op31YnNellNwnktqrsUQbPp0xPMJyYfJza1p6iYAw-ZBF--nUQG7_ebvYCmCXTLZP3sQhJtLkTyMWLITJv-4hcpjES-Nrxgx7-akHb3tblWmMEt7kMvij5nGfP2PI4tf-y53HXkwoi2bNw5fROJfJk7lDa8U9vJrSW3nOmD3iKdQqVkNPNIxp2TUHiZDrxFLS8wzjFg6UdbrXiCmsrbedsen2mrqObU1vmyrj4xFSjaHdKXr_nZ4SDGq4cP4NInc2W_a0gomTmyea02HOpz-SZUBVlFmdgIIXbbZpmq18rDAYEPz0-o5dV96QFqBGbVnLfejbSRt5wH2_Q-BxYa-soHd6mVsmO-zEjdIpXmGeJJm_cncbLiWRMwpWt_c0hPNMqAIKm_u0wDha-B9C6HtbmAXSw7olIv5NBbygmDJJi4ylcNi0p4LD4CxabmlB-dF3cnDaKRYz0ngM2NVirqaqYhyMxIaTvjEcFrnXxxjV61QLLe9khmYlt0_ZWIetCzFw4Ha4l_fM-E-pmSmuEs8fRiL4U0AdJuC40Tg2b4nPpdEERuoJrgLhqSKG-1Xy_tDTQPuwa_d8lxQSbjwbp8Tlfx6_dwIrM2TqC5r2exjpvgaqNHYk2R56zSl-bOkX0Ba2Vxqrf21s0mSleEcuohckQbZvkbDvM5kQpjq8739LxYbjZkZzyeDe57dHNNKRLkTrPibo0ikYgr3G3Azx8__HrP-6QX9-8dOJCrW6o_oi26X7pY40lHSiJ5qcwNsXuPikroPgxDok64QAa0AN8NoSRaTAwjrQ0yAEgUaXcjU7ndLyWg7vNGGmIbAGhyLSoHdS-YlKedz5buEd1_ZIeXE9_v14v3aacQ8IPmOKqfDUzDXmpl-TDmMtITAlUtRN30z2h5fz45JqgNen2B8lLVoJ1FNB4OqetUWDg7iowiFqX9t4wMHCYx6zscNrbY3KdtexGh5gypEc6NQ6tTIz4QB54LPuy-QXsMqUV2lOf1e6BkT9Bdo573Pi-MVSWUEAOwQbJjOR2zLpKDq7zdAN4ZTJS-ruEypLv9VO3UlhBLCxkEH_ebuoeap4zqr7_-Y77nuljV4Fd5tMNrw_TzCntIrFYQPHRc_l-5TTUm-7EWv5ldWesc45mpEj2nltuYT9P3WDp0NTnvVkNsH0XSTNQAbBidtzR-phx2TwNryksHBDNBtsxuHp3tubadhKGyD6LxmYP1qgis0_lmzsFmusMcmX14oHEFcMv1PC3l81JSLdnn2cBNrvBNXwUdPjo-Lo0L89UwFtFpuY4pGkOwXnY5TkikBAs2wxpRgBXLKl9WNaDffF7v-lxmfJe-vFSYjjKK-eG47LCf-ENRGjfq5mTTYfIXol_fcnlyJU_N-zCvo2rWIQO-0xDJ6LR1Wup2lgU2T8F6XFHpsuAU_Hdw3phvCGB5zfnZ_IBKUoxqztNX5kBMPB6ZtmjZLogUabsP9ObZX-Z__gWfTO4NAgYAAA==.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImV4cCI6MTczNjg3MzE1NSwiYWxsb3dBY2Nlc3NPdmVyUHVibGljSW50ZXJuZXQiOnRydWV9",
            "embed_url": "https://app.powerbi.com/reportEmbed?reportId=dc20da54-0dde-4b7e-aa9c-4435bb7c71be&groupId=ceb0d1d0-6226-4aef-b245-fac7f89bb52e&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsidXNhZ2VNZXRyaWNzVk5leHQiOnRydWV9fQ%3d%3d",
            "dataset_id": "4314c162-cd96-46f5-be4c-4e2ed9354b56",
            "csv_files": []
        },
        "025bdeaf-cf4e-40b9-a4c6-01446cbdff3f": {
            "name": "CLOSER_BIACADEMY",
            "pages": [
                {
                    "name": "ad7629625350de3c2f92",
                    "displayName": "Customers",
                    "order": 0
                },
                {
                    "name": "2d7047f129c3f2484ff2",
                    "displayName": "Main Offices",
                    "order": 1
                },
                {
                    "name": "b68cb1241c5ac12d55a6",
                    "displayName": "Dashboard2",
                    "order": 7
                },
                {
                    "name": "7c653908f5a8a0f72bb0",
                    "displayName": "Dashboard1",
                    "order": 6
                },
                {
                    "name": "30e7910a0c74d5ed9130",
                    "displayName": "product_best_worst",
                    "order": 5
                },
                {
                    "name": "e3e8edd15f80dbc7ad77",
                    "displayName": "Sales_quantity_country",
                    "order": 4
                },
                {
                    "name": "50c1abe0586dfc224c03",
                    "displayName": "Sales_quantity_amount_monthCategory",
                    "order": 3
                },
                {
                    "name": "38741aa4f17a9ebc9995",
                    "displayName": "Product_Size_Weight_Color",
                    "order": 2
                }
            ],
            "embed_token": "H4sIAAAAAAAEACWTt66EVgAF_-W1WGLJYMkFOeclduQcLgssYPnf_Sz3U8058_ePk93jkpU_f_5I8t5oVo4QZyr0R4ZUXfrkXrFNJK2SR_CV0fch0ywyJDFZAyvvmkGs7g-cGQe0KcCNu7DTK9YuGYrORDbWgeiuR7I91mU0ZC9LyB7KL4M8HFEjffzgYKXADrmlRo8X9Af4FxUN7fadT2dR0fMzdhjLOy82MYLM_MTphd8JId2jIrQu3n_xdv_iXDCTYVw0X-eQZgwfw_aBpmGb_Z4sDWbzKipKUpcI9F580JdIEEdUeIxE7_JlFHi6nCrD5YaXmV9ndWCY5S9JJSez5CFMfRWHktGoX2hIO843EU4ExlqHpxD7S7HGyUl9oGF7iQre-vSjSJyJnbObakjwt9W_8pjyw8GELnbZ4zBz5wJYsBK1GR73k-8520uvbiUkTt2hKQ3eqlHjFBDxWWVf1McofFHBmGJqxmZt-ZyQOsp3R1EWtTcjFgrisX4XvdIdMltmVEozl0QDOhANo63b3PAl8R-ZK1yLfVWjRrDyi4p4qqLoqBwmg2plyZNsPHLybzUNcRN54s0rX7uQwr5vHFLic-l1kky8YX23-s2k0429JZ6nta02xKAFYmHdk2vJ9sS8L9FOQbC2sQGAW1KnsSxIG9jRrMWejeq1TfAwh0HnKBMPRpiLkZisw2SY-sYMVzYp1aM2IAmlYaxEBxiFgiKVD0rY9EWcl8Xb5mT_LSQN30ojOoyL1qifoOhW1LwoX2MUNHIc8ndalxdS_DIF6vuhLTGUFwSsbPl5Q9cpaVLD8_sshDoqznL1qVb9Yx_pKg8pA90jodI_f_zw273ui17dvzn4E1Hv9pPTWcs6YeF0szPw1doDa3VHs-YEa50XG1DfmTHad1zjCJ0EDC0Gzam_px4C9qeDUoxkFzD6rEKRuJ6BajFTC43hJlTGVvUYHAQsfJMFLVlCQqjb8szKsG9wMXYJxxyew1-BIiBDqY_xMdK_95BM0iotdXkPE6JTQuk9_G-zwSicnNt_2CILytcthk7M-Nc-ZKijZgWr5gwvYFhWMl4ASvvzoGAY2FDZ7uRKPfceZsXZcWDn7eYoKHvzh1mjgZm38JwIL0pWMbvoI01vJshZhHnjBRsWShCkSb-mXGERGOzj0BOVk-yVdZ8A3U375sbltbCLPMGzk0uWkxDJ5q-__tN8r221qeGv5TeR57GZmyeluM2O-ni5l8P_lN81c7YfW_WL1U6OKr362YU6bGe3VGXRO5ENhVG2XqgcWjuGb25lvgJNmXobQ_Z9zXTnfssYNXXXrhip6eNbMqsTKMLQYpg2A4G9WjQ9RFRefg5P44Uj9krJzueGztROJLnr9N-y3jO_VtybPYjYKg2ajjusbAFLNF8O5ThLnwkr9Kw9tfNdhehkno7rSuWnvpgnIJqGe3sI3KBfNK1bUpeigd1s2wtujAcijI6uWwsOMKqIJfTQWkyWmuDGJMt6fipKcBKr86C7rwJPujj7rqF-4BDbWnj7mDBoafnCVcMCZo5c0V8acdqQkUXD0dKfmmFKfJxVfrDqqYONbeydRswGX4gDSbfZ7-3-av7nX_rRlNECBgAA.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImV4cCI6MTczNjg3MzE1NSwiYWxsb3dBY2Nlc3NPdmVyUHVibGljSW50ZXJuZXQiOnRydWV9",
            "embed_url": "https://app.powerbi.com/reportEmbed?reportId=025bdeaf-cf4e-40b9-a4c6-01446cbdff3f&groupId=ceb0d1d0-6226-4aef-b245-fac7f89bb52e&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsidXNhZ2VNZXRyaWNzVk5leHQiOnRydWV9fQ%3d%3d",
            "dataset_id": "7a924e7a-7ab5-4cfb-8e43-df82647bfc20",
            "csv_files": []
        }
    }
};

/**
 * Processes reports for the specified workspaces.
 * Iterates through the workspaces and reports, embeds each report, waits for it to load and render,
 * and then extracts visual data from the report.
 */
async function processReports() {
    for (let workspace in info) {
        for (let reportInfo in workspace) {
            let report = embedPowerBIReport(reportInfo["embed_url"], reportInfo["embed_token"]);

            await reportLoaded;
            console.log("Report loaded successfully.");

            await reportRendered;
            console.log("Report rendered successfully.");

            await extractVisualData(report);
        }
    }
}

// Load the report when the page is ready
$(document).ready(loadAndEditReport);
