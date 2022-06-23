import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:
    _key_: str
    _api_: list
    sheet: discovery

    def __init__(self, key: str, api: list):
        self._key_ = key
        self._api_ = api
        self._connect_()

    def _connect_(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self._key_, self._api_)
        http_auth = credentials.authorize(httplib2.Http())
        self.sheet = discovery.build("sheets", "v4", http=http_auth)
