import sqlite3
from loguru import logger
logger.info("demo")

# singleton
class SqlDb:
    # Class variable

    sql_db: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self):
        self.sql_db = sqlite3.connect('project_12th_db.db')
        self.cursor = self.sql_db.cursor()

    def does_user_exist(self, user_name):
        self.cursor.execute("select * from USERS where user_name like ?", (user_name,))
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            return True
        else:
            return False

    def add_user(self, user_name, phone, password):
        if not self.does_user_exist(user_name):
            self.cursor.execute("insert INTO USERS (USER_NAME,password,phone,lat,lng) VALUES (?,?,?,?,?)",
                                (user_name, password, phone,0,0))
            self.sql_db.commit()
            return True
        return False

    def update_location(self, user_name, lat,lng):
        if self.does_user_exist(user_name):
            self.cursor.execute("update users set lat = ?, lng = ? where user_name like ?",(lat,lng,user_name))
            self.sql_db.commit()
            return True
        return False

    def get_Location(self,user_name):
        rows = 0
        logger.debug(user_name)
        if self.does_user_exist(user_name):
            self.cursor.execute("select lat,lng from users where user_name like ?",(user_name,))
            rows = self.cursor.fetchall()
        
        logger.debug(rows)    
        return rows


    def does_pass_and_username_match(self, user_name, password):
        self.cursor.execute("select * from USERS where user_name like ? and password = ?", (user_name, password))
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            return True
        else:
            return False
