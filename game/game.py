#!/usr/bin/env python
# standard width = 10, standard height = 22

import random
from threading import Thread
from time import sleep
from tetromino import tetromino
from tetromino import point
from tetromino import matrice
import persist

class Game(Thread):
    figures = ['I','J','L','O','S','T','Z']
    # figures = ['I', 'O']
    def __init__(self, width, height, app):
        Thread.__init__(self)
        self.width = width
        self.height = height
        self.app = app
        self.stop = 0
        self.running = 0
        self.current = None
        self.direction = None
        self.matrice = matrice.Matrice(width + 2, height + 1)
        self.imageMatrice = []
        self.score = 0
        self.initMatriceBase()
        self.over = 0

        self.persistence = persist.Persist()
        scores = self.persistence.getScores()
        self.max = 0
        for s in scores:
            if self.max < s.score : self.max = s.score
        self.app.textvarBest.set(str(self.max))

    def initMatriceBase(self):
        for i in range(0, self.width + 2):
            self.matrice.body[self.height][i] = 1
        for j in range(0, self.height):
            self.matrice.body[j][self.width + 1] = 1
            self.matrice.body[j][0] = 1

    def randomize(self):
        return tetromino.Tetromino(random.choice(self.figures))

    def run(self):
        self.next = self.randomize()
        self.running = 1
        while not self.stop:
            self.progressCurrent()

        if self.over :
            self.app.writeFlashyText('GAME OVER')
        self.running = 0
        if self.score > 0:
            persistScore = persist.Score(self.score)
            persistScore.doPersist()


    def progressCurrent(self):
        hitBottom = 0
        self.current = self.next
        self.next = self.randomize()

        buffNext = tetromino.Tetromino(self.next.form)
        buffCurrent = tetromino.Tetromino(self.current.form)
        self.app.drawTetromino(self.app.canvasNext, buffNext, point.Point(0,1))
        self.app.drawTetromino(self.app.canvasHold, buffCurrent, point.Point(0,1))

        p = point.Point(3,1)
        while (not hitBottom and not self.stop) :
            self.app.clearTetromino(self.app.canvas, self.current)
            self.gotoDirection(p)

            hitBottom = self.hitMatrice(p)
            if(hitBottom and p.y == 1):
                self.stop = 1
                self.over = 1
            if not hitBottom :
                p.translate(point.Point(0,-1))
            self.app.drawTetromino(self.app.canvas, self.current, p)
            sleep(0.2)

        self.app.clearTetromino(self.app.canvas, self.current)

        p.translate(point.Point(-1, 0))
        self.matrice.merge(self.current.points, p)

        self.baseFilled()
        self.app.drawMatrice(self.matrice)

        self.app.clearTetromino(self.app.canvasNext, buffNext)
        self.app.clearTetromino(self.app.canvasHold, buffCurrent)

    def hitMatrice(self, translator):
        for p in self.current.points:
            m = p.y + translator.y + 1
            n = p.x + translator.x + 1
            if m >= len(self.matrice.body): continue
            if n >= len(self.matrice.body[m]) : continue
            if self.matrice.body[m][n] == 1 : return 1
        return 0

    def unavailableDirections(self, translator):
        directions = []
        for p in self.current.points:
            m = p.y + translator.y + 1
            n = p.x + translator.x + 1
            if self.matrice.get(m, n) == 1 : directions.append('Down')
            if self.matrice.get(m, n - 1) == 1 : directions.append('Left')
            if self.matrice.get(m, n + 1) == 1 : directions.append('Right')
        return directions

    def baseFilled(self):
        for i in range(1,self.matrice.n - 1):
            full = 1
            for j in range(1,self.matrice.m - 1):
                if self.matrice.get(i,j) != 1 :
                    full = 0
                    break
            if full:
                self.score += 3
                self.app.textvarScore.set(str(self.score))
                self.matrice.slice(i)
                self.app.drawMatrice(self.matrice)
                sleep(0.3)


    def gotoDirection(self, p):
        forbiden = self.unavailableDirections(p)
        if(self.direction in forbiden): return
        if (self.direction == 'Left') :
            p.translate(point.Point(1,0))
        if self.direction == 'Right':
            p.translate(point.Point(-1,0))
        if self.direction == 'Up':
            self.current.rotate()

        self.direction = None
