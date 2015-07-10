#!/usr/bin/env python

class Matrice():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.body = []
        for i in range(0,n):
            self.body.append([])
            for j in range(0,m):
                self.body[i].append(0)


    def toString(self):
        res = ''
        for i in range(0,self.n):
            for j in range(0,self.m):
                res += "%d " % (self.body[i][j])
            res += "\n"
        return res

    def merge(self, points, translator):
        for p in points:
            m = p.y + translator.y
            n = p.x + translator.x
            if m >= len(self.body): continue
            if n >= len(self.body[m]) : continue
            self.body[m][n] = 1

    def slice(self, n):
        for i in range(n, 0, -1):
            for j in range(0, self.m):
                self.body[i][j] = self.body[i - 1][j]

    def get(self, m, n):
        if m >= len(self.body): return None
        if n >= len(self.body[m]) : return None
        return self.body[m][n]
