import sqlite3
from abc import ABCMeta, abstractmethod


class Conn(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class SQLiteConnect(Conn):

    __slots__ = ['__name', '__connection']

    def __init__(self, name='sqlite3.db'):
        self.__name = name
        self.__connection = None

    def __str__(self) -> str:
        return f'SQLiteConnect({self.__name})'

    @property
    def name(self):
        return self.__name

    @property
    def connection(self):
        return self.__connection

    def connect(self):
        self.__connection = sqlite3.connect(self.__name)

    def disconnect(self):
        try:
            self.__connection.close()
        except AttributeError:
            pass


class ConnectionFactory():

    __slots__ = ['__name']

    def __init__(self, name: str):
        self.__name: str = name

    def __str__(self) -> str:
        return f'ConnectionFactory({self.__name})'

    def make(self):
        return eval(self.__name)()


class Model():

    __slots__ = ['__connection']

    def __init__(self, connection):
        self.__connection = connection

    def __str__(self) -> str:
        return f'Table()'

    def create(self):
        try:
            cursor = self.__connection.cursor()

            # cursor.execute("DROP TABLE IF EXISTS clients;")

            query = """
            CREATE TABLE IF NOT EXISTS clients(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL
            )
            """
            cursor.execute(query)
        except AttributeError as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return f'Error, connection'

    def insert(self, name, cpf, email):
        try:
            cursor = self.__connection.cursor()

            try:

                cursor.execute("""
                                INSERT INTO clients (name, cpf, email) VALUES (?,?,?)
                                """, (name, cpf, email))
                self.__connection.commit()
            except sqlite3.IntegrityError as e:
                import logging
                logger = logging.getLogger(__name__)
                logger.exception(e)
                return f'Error, cpf {cpf} exists'

        except AttributeError as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return f'Error, connection'

    def find(self, cpf):
        try:
            cursor = self.__connection.cursor()

            try:

                cursor.execute("""SELECT * FROM clients WHERE cpf=?""", (cpf,))
                record = cursor.fetchone()
                return record
                cursor.close()
            except sqlite3.IntegrityError as e:
                import logging
                logger = logging.getLogger(__name__)
                logger.exception(e)
                return f'Error, cpf {cpf} exists'

        except AttributeError as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return f'Error, connection'
        
    
    def find_all(self):
        try:
            cursor = self.__connection.cursor()

            try:

                cursor.execute("""SELECT * FROM clients""")
                records = cursor.fetchall()
                output = []
                for row in records:
                    output.append(f'id: {row[0]}, cpf: {row[2]}, name: {row[1]}, email: {row[3]}')
                
                return output
                
            except sqlite3.IntegrityError as e:
                import logging
                logger = logging.getLogger(__name__)
                logger.exception(e)
                return f'Error, connection'

        except AttributeError as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return f'Error, connection'

    def delete(self, cpf):
        try:
            cursor = self.__connection.cursor()

            record = self.find(cpf)
            cursor.execute("""DELETE FROM clients WHERE cpf = %s""" % cpf)
            self.__connection.commit()
            if self.find(cpf) != 'None':
                return f'O cliente foi removido com sucesso.'

        except AttributeError as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return f'Error, connection'
