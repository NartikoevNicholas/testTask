import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


class ServiceAccount:
    _key: str
    _api: list
    account: discovery

    def __init__(self, key: str, api: list):
        self._key = key
        self._api = api
        self._connect()

    def _connect(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self._key, self._api)
        http_auth = credentials.authorize(httplib2.Http())
        self.account = discovery.build("sheets", "v4", http=http_auth)
