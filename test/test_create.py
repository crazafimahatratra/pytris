#!/usr/bin/env python
import unittest
from tetromino import tetromino

# I, J, L, O, S, T, Z
class TestCreate(unittest.TestCase):
    def setUp(self):
        pass

    def test_createI(self):
        t = tetromino.Tetromino('I')
        self.assertEqual(t.matrice, [[0, 1],[1, 1],[2, 1],[3, 1]])
        self.assertEqual(t.color, 'cyan')

    def test_createJ(self):
        t = tetromino.Tetromino('J')
        self.assertEqual(t.matrice, [[0, 0],[0, 1],[1, 1],[2, 1]])
        self.assertEqual(t.color, 'blue')

    def test_createL(self):
        t = tetromino.Tetromino('L')
        self.assertEqual(t.matrice, [[0, 1],[1, 1],[2, 1],[2, 0]])
        self.assertEqual(t.color, 'orange')

    def test_createO(self):
        t = tetromino.Tetromino('O')
        self.assertEqual(t.matrice, [[1, 0],[2, 0],[1, 1],[2, 1]])
        self.assertEqual(t.color, 'yellow')

    def test_createS(self):
        t = tetromino.Tetromino('S')
        self.assertEqual(t.matrice, [[0, 1],[1, 1],[1, 0],[2, 0]])
        self.assertEqual(t.color, 'green')

    def test_createT(self):
        t = tetromino.Tetromino('T')
        self.assertEqual(t.matrice, [[1, 0],[0, 1],[1, 1],[2, 1]])
        self.assertEqual(t.color, 'purple')

    def test_createZ(self):
        t = tetromino.Tetromino('Z')
        self.assertEqual(t.matrice, [[0, 0],[1, 0],[1, 1],[2, 1]])
        self.assertEqual(t.color, 'red')

    def test_createX(self):
        self.assertRaises(Exception, tetromino.Tetromino, 'X')
