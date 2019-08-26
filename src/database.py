import psycopg2
import configparser


class Database:
    def __init__(self, configfile):
        self._conn = None
        params = self.config(filename=configfile)
        try:
            self.connect(params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def __del__(self):
        if self._conn is not None:
            self._conn.close()
            print('Database connection closed.')

    @staticmethod
    def config(filename='database.ini', section='postgresql'):
        # create a parser
        parser = configparser.ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    def connect(self, params):
        print('Connecting to PostgreSQL database...')
        self._conn = psycopg2.connect(**params)
        cur = self._conn.cursor()
        print('Select version...')
        cur.execute('SELECT version()')
        print('Display version...')
        db_version = cur.fetchone()
        print(db_version)
