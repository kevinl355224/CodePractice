import psycopg2

class Db_process:
    
    def __init__(self):
        self.conn = None
        try :
            #嘗試連結render資料庫，開始專案底下的external外部連結
            self.conn = psycopg2.connect(
                    host ="dpg-EEEE.oregon-postgres.render.com",
                    dbname = "xxxx",
                    user = "xxxx_user",
                    password = "AAAA"
                    )   
            print("Connection Success")
        except psycopg2.Error as err:
            print("Connection Fail")
            print(str(err))
    
    #增加刪除物件
    def __del__(self):
        if self.conn is not None:
            self.conn.close()
            print("Database Closed")
    
    #讀取
    def read(self,sql):
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            datas = cur.fetchall()
            print(datas)
            print("//Reading success//")
            return datas
        except psycopg2.Error as err:
            print("Reading Fail")
            print(str(err))
        cur.close()
    
    #增加資料
    def write(self,sql,value=None):
        cur = self.conn.cursor()
        try: 
            cur.execute(sql,value)
            self.conn.commit()
            print("//Writing success//")
        except psycopg2.Error as err:
            print("Writing Fail")
            print(str(err))
        cur.close()
    
    #增加多筆資料
    def write_muti(self,sql,value):
        cur = self.conn.cursor()
        try:
            cur.executemany(sql,value)
            self.conn.commit()
            print("//Write_muti success//")
        except psycopg2.Error as err:
            print("Writing_muti Fail")
            print(str(err))
        cur.close()

    #刪除資料
    def delete(self,sql,value=None):
        self.write(sql,value)
        print("Deleted Success")
##Test_Code

# db = Db_progress()
# #sql = "delete from demo where id = 4"
# #sql = "update Demo set passwd =66 where account = 'user66' "

# #data = [('user11','pwd11'),('user22','pwd22'),('user33','pwd33')]
# #db.delete(sql)

# # sql = "insert into Demo(account,passwd) values('user66','pwd66')"
# # db.write(sql)

# sql = "SELECT * FROM DEMO"
# db.read(sql)