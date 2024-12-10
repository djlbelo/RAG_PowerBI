import requests


class PowerBIWidelySharedArtifacts:
    API_VERSION = '2017-10-01'
    BASE_URL = 'https://api.powerbi.com/v1.0/myorg/admin'

    @staticmethod
    def links_shared_to_whole_organization(headers):
        url = f'{PowerBIWidelySharedArtifacts.BASE_URL}/widelySharedArtifacts/linksSharedToWholeOrganization?api-version={PowerBIWidelySharedArtifacts.API_VERSION}'
        response = requests.get(url, headers=headers)
        return response.json()