import requests


class Bot:

    _url_: str
    _channel_id_: str

    def __init__(self, token: str, channel_id):
        self._url_ = "https://api.telegram.org/bot" + token
        self._channel_id_ = channel_id

    def send_message(self, message: str):
        method = self._url_ + Method.SEND_MESSAGE
        requests.post(method, data={"chat_id": self._channel_id_, "text": message})


class Method:
    SEND_MESSAGE = "/sendMessage"
    GET_ME = "/getMe"