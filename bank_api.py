__author__ = 'alexanderstolz'

import hib_sql_connection



def getAllTransfers():
    connection = hib_sql_connection.connectToHibiscus()
    return hib_sql_connection.queryToHibiscus(connection, "select * from umsatz;")

def getOutgoingTransfers():
    connection = hib_sql_connection.connectToHibiscus()
    return hib_sql_connection.queryToHibiscus(connection, "select * from umsatz where betrag < 0;")

def getIncomingTransfers():
    connection = hib_sql_connection.connectToHibiscus()
    return hib_sql_connection.queryToHibiscus(connection, "select * from umsatz where betrag > 0;")