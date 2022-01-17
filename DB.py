import mysql.connector
# from mysql.connector import Error

# pip3 install mysql-connector
# https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html

class DB():
    def __init__(self):
        self.connection = None
        self.connection = mysql.connector.connect(host="localhost", user="phpmyadmin", password="djarafat10", database="python_poo")
        
    def query(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor

    def insert(self,sql,args):
        cursor = self.query(sql, args)
        id = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return id

    # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html
    def insertmany(self,sql,args):
        cursor = self.connection.cursor()
        cursor.executemany(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount

    def update(self,sql,args):
        cursor = self.query(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount

    def fetch(self, sql):
        rows = []
        cursor = self.query(sql)
        if cursor.with_rows:
            rows = cursor.fetchall()
        cursor.close()
        return rows

    def fetchone(self, sql, args):
        row = None
        cursor = self.query(sql, args)
        if cursor.with_rows:
            row = cursor.fetchone()
        cursor.close()
        return row

    def __del__(self):
        if self.connection != None:
            self.connection.close()