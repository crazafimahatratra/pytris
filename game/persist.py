#!/usr/bin/env python
import sqlite3 as db
import time

class Score():
    dt = None
    score = 0
    def __init__(self, score):
        self.score = score
        self.dt = time.strftime('%Y-%m-%d %H:%M:%S')

    def doPersist(self):
        p = Persist()
        p.insertScore(self.dt, self.score)

class Persist():
    dbname = 'tetris.db'
    tablename = 'score'
    def __init__(self):
        self.initDb()
        pass

    def verifDd(self):
        conn = db.connect(self.dbname)
        query = '''SELECT name FROM sqlite_master WHERE type = "table" AND name='%s' ''' % (self.tablename)
        cursor = conn.execute(query)
        i = 0
        for row in cursor: i+=1
        conn.close()
        return i

    def initDb(self):
        if self.verifDd():
            return
        conn = db.connect(self.dbname)
        conn.execute('''CREATE TABLE %s(
                dt datetime,
                score int
            )
        ''' % (self.tablename))
        conn.close()

    def insertScore(self, dt, score):
        conn = db.connect(self.dbname)
        query = ('''INSERT INTO %s(dt, score) VALUES('%s','%d')''' % (self.tablename, dt, score))
        conn.execute(query)
        conn.commit()
        conn.close()

    def getScores(self):
        conn = db.connect(self.dbname)
        query = '''SELECT dt,score FROM %s ORDER BY dt''' % (self.tablename)
        cursor = conn.execute(query)
        res = []
        for i in cursor:
            s = Score(i[1])
            s.dt = i[0]
            res.append(s)

        conn.close()
        return res
