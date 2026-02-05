import sqlite3


class Database:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def read_from_db(self):
        pass

    def write_to_db(self, number):
        pass
