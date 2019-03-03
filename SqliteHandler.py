import sqlite3
from sqlite3 import Error
        
class SqliteDataHandler:
    def __init__(self):
        self.databasepath="Fantasyc.db"
        self.conn = sqlite3.connect('Fantasyc.db')
        self.curser = self.conn.cursor()

    def FetachTeams(self):
        squery="select distinct name from teams;"
        self.curser.execute(squery)
        teams = self.curser.fetchall()
        return teams

    def FetchItems(self,squery):
        self.curser.execute(squery)
        teams = self.curser.fetchall()
        return teams

    def Fetchcoloumns(self,squery):
        self.curser.execute(squery)
        teams = self.curser.fetchall()
        return self.curser

    def InsertItems(self,squery,data):

        try:
            print(squery,data)
            self.curser.execute(squery, data)
            self.conn.commit()
            return "1"
        except:
            return "0"




# def createConnection(db_file):
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
#     return None
#
# def searchFiles(dbfile,searchtext,searchdrive):
#     conn=createConnection(dbfile)
#     cur = conn.cursor()
# ##    sdrives = tuple(searchdrive)
# ##    cur.execute("SELECT * FROM indexedFiles where file like '%{}%' and drive in {}".format(searchtext,sdrives))
#     cur.execute("SELECT * FROM indexedFiles where file like '%{}%'".format(searchtext))
#     rows = cur.fetchall()
#     searched_files=[row[2] for row in rows]
#     return searched_files
#     conn.close()
#
# def getFileType(dbfile):
#     conn=createConnection(dbfile)
#     cur = conn.cursor()
# ##    sdrives = tuple(searchdrive)
# ##    cur.execute("SELECT * FROM indexedFiles where file like '%{}%' and drive in {}".format(searchtext,sdrives))
#     cur.execute("SELECT distinct type FROM indexedFiles")
#     rows = cur.fetchall()
#     searched_files=[row[0] for row in rows]
#     return searched_files
#     conn.close()
#
# def insertFile(dbfile,data):
#     try:
#         conn=createConnection(dbfile)
#         with conn:
#             for d in data:
#                 cur = conn.cursor()
#                 sql = ''' INSERT OR IGNORE INTO indexedFiles(drive,file,type) VALUES(?,?,?) '''
#                 cur = conn.cursor()
#                 cur.execute(sql, d)
#
#     except:
#         print('Alredy exists')
#
