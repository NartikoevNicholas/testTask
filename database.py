import psycopg2


class Database:
    _name_: str
    _user_: str
    _password_: str
    _host_: str
    _port_: str
    connect: psycopg2

    def __init__(self, name: str, user: str, password: str, host: str, port: str):
        self._name_ = name
        self._user_ = user
        self._password_ = password
        self._host_ = host
        self._port_ = port
        self._connection_()
        self.connect.autocommit = True

    def _connection_(self):
        self.connect = psycopg2.connect(
            database=self._name_,
            user=self._user_,
            password=self._password_,
            host=self._host_,
            port=self._port_)
