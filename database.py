import psycopg2


class Database:
    name: str
    user: str
    password: str
    host: str
    connect: psycopg2

    def __init__(self, name: str, user: str, password: str, host: str):
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self._connection()
        self.connect.autocommit = True

    def _connection(self):
        self.connect = psycopg2.connect(database=self.name, user=self.user, password=self.password, host=self.host)
