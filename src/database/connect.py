# from time import time
from psycopg2 import connect


def database():
    try:
        sql = connect(host='localhost', dbname='python',
                      user='user', password='password', port=5432)
        cursor = sql.cursor()
        return cursor
    except Exception as err:
        print(err)
        # time.sleep(2)
