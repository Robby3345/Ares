import pymysql


class SqlHelper(object):
    def __init__(self, db):
        self.db = db
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, database=self.db,
                                    charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def get_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def modify(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()
