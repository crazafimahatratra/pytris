#!/usr/bin/env python
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None

    def toString(self):
        return "(%d,%d)" % (self.x, self.y)

    def translate(self, O):
        x = int(self.x) - O.x
        y = int(self.y) - O.y
        self.x = x
        self.y = y

    def inverse(self):
        self.x = -self.x
        self.y = -self.y

    def rotate(self, center):
        self.translateByCenter(center)
        self.rotateBy90()
        self.backFromTranslation(center)

    def translateByCenter(self, center):
        self.translate(center)

    def rotateBy90(self):
        theta = math.radians(-90)
        x = int(self.x*math.cos(theta)) + int(self.y*math.sin(theta))
        y = int(-self.x*math.sin(theta)) + int(self.y*math.cos(theta))
        self.x = int(x)
        self.y = int(y)

    def backFromTranslation(self, center):
        center.inverse()
        self.translate(center)
