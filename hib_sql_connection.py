__author__ = 'alexanderstolz'


import pymysql.cursors
import pymysql

# Connect to the database
def connectToHibiscus():
    connection = pymysql.connect(host='localhost',
                                 user='hibiscus',
                                 password='c3zSsuQYVJsy9vRB',
                                 db='hibiscus',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def queryToHibiscus(connection, sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()
