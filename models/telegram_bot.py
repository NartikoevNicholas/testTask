import telegram_send


class Bot:
    @staticmethod
    def message_send(message: str):
        telegram_send.send(messages=[message])
