#!/usr/bin/env python
from tetromino import Point
class Rectangle():
    def __init__(self, p, width, height):
        self.x0 = p.x
        self.y0 = p.y
        self.x1 = self.x0 + 1
        self.y1 = self.y0 + 1
        self.width = width
        self.height = height

    def translate(self, x, y):
        self.x0 = x - self.x0
        self.y0 = y - self.y0
        self.x1 = x - (self.x1 + 1)
        self.y1 = y - (self.y1 + 1)

    def hMirror(self, y):
        self.y0 = y - self.y0
        self.y1 = self.y0 - 1

    def homothetie(self):
        self.x0 *= self.width
        self.y0 *= self.height
        self.x1 *= self.width
        self.y1 *= self.height
