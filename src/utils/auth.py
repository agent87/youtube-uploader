from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


def get_authenticated_service(
    client_secrets_file: str, scopes: str, api_service_name: str, api_version: str
) -> build:
    """A function to authenticate and store credentials"""
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    return build(api_service_name, api_version, credentials=credentials)


class AuthenticationController:
    """The authentication controller"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_authenticated_service(
        client_secrets_file: str, scopes: str, api_service_name: str, api_version: str
    ) -> build:
        """A function to authenticate and store credentials"""
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_console()
        return build(api_service_name, api_version, credentials=credentials)
