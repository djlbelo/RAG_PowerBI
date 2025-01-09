import powerbi from 'powerbi-client';
import * as models from 'powerbi-models';


const AUTHORITY_URL = 'https://login.microsoftonline.com/organizations';
const CLIENT_ID = '04bb970d-3099-4845-b81d-92e23362f261';
const SCOPE = [
    "https://api.fabric.microsoft.com/Dataset.ReadWrite.All",
    "https://api.fabric.microsoft.com/Dashboard.ReadWrite.All",
    "https://api.fabric.microsoft.com/Item.ReadWrite.All",
    "https://api.fabric.microsoft.com/Workspace.ReadWrite.All",
    "https://api.fabric.microsoft.com/Report.ReadWrite.All",
    "https://api.fabric.microsoft.com/Content.Create"
];

const GROUP_ID = 'ceb0d1d0-6226-4aef-b245-fac7f89bb52e';
const POWER_BI_API_URL = 'https://api.powerbi.com/v1.0/myorg/';
const TENANT_ID = '057866cb-0e0f-4818-bd4a-0255845df359';

const REPORT_ID = 'dc20da54-0dde-4b7e-aa9c-4435bb7c71be';
const EMBED_TOKEN = "H4sIAAAAAAAEAB3Ux66zVgAE4He5WyLRW6R_AQZsmul1RwdTDj50orx7rrIfaaRPo_nnx86uAWTlz98_x8agA6LxpHM96eCyUmvPV9zxKXhZ_r4HgUtYDB_vmUyM32cKp0C-oa127bzQ4Rmtvk4YynNcWiwLc8hNQVD1017B0eV06kLxl-iy_o31lzvGs4J2hlZRntmmNaPJ38p7cBvqbKf-IUYoT-u8pB_Em1nKzKodCZfXLVpCnOj5q-jO-XDFIRGnEfgtzSyeJD74jM8qeFbk1AU0t-09wdmGuKIWiC0IFObR0lrUNh-aHDxSnjmTb8cjW58EeJkY31SKi9nxVCCUrme62TMdhWRzn3BwcWfVe6hMCXrAv8yMAIZGD0wnf1JNbV3bi4yvlssrid7H_AS7noG120ct6_rYK-dTZdzG2xHWjxXavM_ns43ZRjpPtovY5b2qEXB966kaqltD_wypPZpw3_oSDCaXBQZpCs_R1z7GRxe3bvkmP5lBgo4nx84MDm8FTWEZuMIrm50dsWvAJHuwXWoBH5ahY2HL4efepdd1iA70NG5ohKQSCmhBE47OdUa7MQtKMB2g4AT27MhQe35h2SO9vy38AhxnBRMn9sYDg6vsBXO42md7l99zCD64AWznRDWBTO4eZR0rsQkUTt_siq1lGx0g4BkTvYFV87vcOwTtP76EdG6WUX9iWxS31Nj8td6bt-S_gqszxpI_NqVfBQLFbVv0FucsWAIrXbVrhJknJHD0ix3I6GTYQQEvbqDWo2DLLOzTtvcV25u0oCowtQLlhMxsAwfondb9lUNpNlNlYKWyPBbsz89fPw94zSvQq-t3-kEY7qPQxIbO6fda46-wLZKzWkQu_Pb2KE3ycVLrXj1lEXsaEX2NBFtf1TYzMhMu7OXtTkvu6rG1Ljd0bSJz-rrqhKf2NEcHAmazbBq45uTX7CiS3WPJHEDl3cmWHSb6rxmHXP4KSzM_Lkpq_In_7fA_yUljW-Y2RbM2YcDimC91rS_HVLUM395f3bv2S7ImfM_AqNpYEyMn4ilJSweYh9tClvk4qmUR_CehGhQV6-l0KT9QbucGyZcYiswUiPLJNt98mvVz2HVuatj6ZbyhnHg5fHmKVFbJrfERwQkD93mTb1aLAoQdD35EMH4Jb8cuQBMhzNbDi42CBJJhi1lpdwb88ed_5mtuK6iGv8oesBuuGlxMUbVWe3yGwI0S4f-U1zVTtm6w-o0NiPTO4JqwC6irj7hXc9Mr3yJq5La6QXgwFn5_1nLtrkvLfs1qYWVYxnIveajaU5pe91RZX7U48QXV99asdxN950DHyzLRcpFRstl8CPSEMdDN35acvRE9_P0HSzijUUnRT83Evaan1XibKZTGolZRPrpgKctDG5ltlz_fxFaQVvp1YWtnRKlW5abqQnvimeQVV09ccF_C2RyyYhBMykF4Ar0Lcns0UtSoCkPYn3sJo1GK5Wr1kPe0VjT_LQkEP-9eW9lJF9EmREfAF-SAcAGeQQCmF60VqZ0zUsS3B32Elf6YICKae6fOXNlw8pt_DHhoTmr3jJZvbmnPPXyhj4doxy_nl_nf_wCOooHF7gUAAA==.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImV4cCI6MTczNTgyMDU2OCwiYWxsb3dBY2Nlc3NPdmVyUHVibGljSW50ZXJuZXQiOnRydWV9";
const EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=dc20da54-0dde-4b7e-aa9c-4435bb7c71be&groupId=ceb0d1d0-6226-4aef-b245-fac7f89bb52e&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsidXNhZ2VNZXRyaWNzVk5leHQiOnRydWV9fQ%3d%3d";


// Set up the configuration object that determines what to embed and how to embed it.
let embedConfiguration = {
    accessToken: EMBED_TOKEN,
    embedUrl: EMBED_URL,
    id: REPORT_ID,
    permissions: somePermissions,
    tokenType: aTokenType,
    type: 'report'
};

// Get a reference to the HTML element that contains the embedded report.
let embedContainer = $('#embedContainer')[0];

// Embed the report.
let report = powerbi.embed(embedContainer, embedConfiguration);