#!/usr/bin/env python
import random
from game import game
from tetromino import tetromino
from tetromino import matrice
from tetromino import point

m = matrice.Matrice(10,10)
t = tetromino.Tetromino('J')
m.merge(t.points, point.Point(0,1))
print m.toString()
m.slice(5)
print m.toString()
