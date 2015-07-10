#!/usr/bin/env python
from point import Point

class Tetromino():
    def __init__(self, form):
        self.form = form
        self.matrice = None
        self.color = None
        self.center = None
        self.points = []
        self.create()
        self.numRotate = 0

    def createPointsFromMatrice(self):
        for i in self.matrice:
            p = Point(i[0], i[1])
            self.points.append(p)

    def create(self):
        if self.form == 'I':
            self.matrice = [[0, 1],[1, 1],[2, 1],[3, 1]]
            self.color = 'cyan'
            self.createPointsFromMatrice()
            self.center = Point(2,1)
            return

        if self.form == 'J':
            self.matrice = [[0, 0],[0, 1],[1, 1],[2, 1]]
            self.color = 'blue'
            self.createPointsFromMatrice()
            self.center = Point(1,1)
            return

        if self.form == 'L':
            self.matrice = [[0, 1],[1, 1],[2, 1],[2, 0]]
            self.color = 'orange'
            self.createPointsFromMatrice()
            self.center = Point(1,1)
            return

        if self.form == 'O':
            self.matrice = [[1, 0],[2, 0],[1, 1],[2, 1]]
            self.color = 'yellow'
            self.createPointsFromMatrice()
            self.center = Point(1,1)
            return

        if self.form == 'S':
            self.matrice = [[0, 1],[1, 1],[1, 0],[2, 0]]
            self.color = 'green'
            self.createPointsFromMatrice()
            self.center = Point(1,1)
            return

        if self.form == 'T':
            self.matrice = [[1,0],[0, 1],[1, 1],[2, 1]]
            self.color = 'purple'
            self.createPointsFromMatrice()
            self.center = Point(1,1)
            return

        if self.form == 'Z':
            self.matrice = [[0, 0],[1, 0],[1, 1],[2, 1]]
            self.color = 'red'
            self.createPointsFromMatrice()
            self.center = Point(1,1)
            return

        raise (Exception, 'No such form')

    def getMatrice(self):
        self.matrice = []
        for i in self.points:
            self.matrice.append([i.x, i.y])
        return self.matrice

    def rotateI(self):
        if self.numRotate == 4 : self.numRotate = 0
        if self.numRotate == 0:
            self.points = [Point(2,0), Point(2,1), Point(2,2), Point(2,3)]
        if self.numRotate == 1:
            self.points = [Point(3,2), Point(2,2), Point(1,2), Point(0,2)]
        if self.numRotate == 2:
            self.points = [Point(1,3), Point(1,2), Point(1,1), Point(1,0)]
        if self.numRotate == 3:
            self.points = [Point(3,1), Point(2,1), Point(1,1), Point(0,1)]
        self.numRotate += 1

    def rotate(self):
        if self.form == 'O': return
        if self.form == 'I':
            self.rotateI()
            return
        for i in self.points:
            center = Point(self.center.x, self.center.y)
            i.rotate(center)
