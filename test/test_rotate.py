#!/usr/bin/env python
import unittest
from tetromino import tetromino

class TestRotate(unittest.TestCase):
    def setUp(self):
        pass

    # rotate I
    def test_rotateI1(self):
        t = tetromino.Tetromino('I')
        t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 0],[2, 1],[2, 2],[2, 3]])

    def test_rotateI2(self):
        t = tetromino.Tetromino('I')
        for i in range(0,2):t.rotate()
        self.assertEqual(t.getMatrice(), [[3, 2],[2, 2],[1, 2],[0, 2]])

    def test_rotateI3(self):
        t = tetromino.Tetromino('I')
        for i in range(0,3):t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 3],[1, 2],[1, 1],[1, 0]])

    def test_rotateI4(self):
        t = tetromino.Tetromino('I')
        for i in range(0,4):t.rotate()
        self.assertEqual(t.getMatrice(), [[3, 1],[2, 1],[1, 1],[0, 1]])


    # rotate J
    def test_rotateJ1(self):
        t = tetromino.Tetromino('J')
        t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 0],[1, 0],[1, 1],[1, 2]])

    def test_rotateJ2(self):
        t = tetromino.Tetromino('J')
        for i in range(0,2): t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 2],[2, 1],[1, 1],[0, 1]])

    def test_rotateJ3(self):
        t = tetromino.Tetromino('J')
        for i in range(0,3):t.rotate()
        self.assertEqual(t.getMatrice(), [[0, 2],[1, 2],[1, 1],[1, 0]])

    def test_rotateJ4(self):
        t = tetromino.Tetromino('J')
        for i in range(0,4):t.rotate()
        self.assertEqual(t.getMatrice(), [[0, 0],[0, 1],[1, 1],[2, 1]])


    # rotate L
    def test_rotateL1(self):
        t = tetromino.Tetromino('L')
        t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 0],[1, 1],[1, 2],[2, 2]])

    def test_rotateL2(self):
        t = tetromino.Tetromino('L')
        for i in range(0,2): t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 1],[1, 1],[0, 1],[0, 2]])

    def test_rotateL3(self):
        t = tetromino.Tetromino('L')
        for i in range(0,3): t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 2],[1, 1],[1, 0],[0, 0]])

    def test_rotateL4(self):
        t = tetromino.Tetromino('L')
        for i in range(0,4): t.rotate()
        self.assertEqual(t.getMatrice(), [[0, 1],[1, 1],[2, 1],[2, 0]])


    # rotate O
    def test_rotateO1(self):
        t = tetromino.Tetromino('O')
        for i in range(0,3): t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 0],[2, 0],[1, 1],[2, 1]])


    # rotate S
    def test_rotateS1(self):
        t = tetromino.Tetromino('S')
        t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 0],[1, 1],[2, 1],[2, 2]])

    def test_rotateS2(self):
        t = tetromino.Tetromino('S')
        for i in range(0,2): t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 1],[1, 1],[1, 2],[0, 2]])

    def test_rotateS3(self):
        t = tetromino.Tetromino('S')
        for i in range(0,3): t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 2],[1, 1],[0, 1],[0, 0]])

    def test_rotateS4(self):
        t = tetromino.Tetromino('S')
        for i in range(0,4): t.rotate()
        self.assertEqual(t.getMatrice(), [[0, 1],[1, 1],[1, 0],[2, 0]])


    # rotate T
    def test_rotateT1(self):
        t = tetromino.Tetromino('T')
        t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 1],[1, 0],[1, 1],[1, 2]])

    def test_rotateT2(self):
        t = tetromino.Tetromino('T')
        for i in range(0,2): t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 2],[2, 1],[1, 1],[0, 1]])

    def test_rotateT3(self):
        t = tetromino.Tetromino('T')
        for i in range(0,3): t.rotate()
        self.assertEqual(t.getMatrice(), [[0, 1],[1, 2],[1, 1],[1, 0]])

    def test_rotateT4(self):
        t = tetromino.Tetromino('T')
        for i in range(0,4): t.rotate()
        self.assertEqual(t.getMatrice(), [[1, 0],[0, 1],[1, 1],[2, 1]])


    # rotate Z
    def test_rotateZ1(self):
        t = tetromino.Tetromino('Z')
        t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 0],[2, 1],[1, 1],[1, 2]])

    def test_rotateZ2(self):
        t = tetromino.Tetromino('Z')
        for i in range(0,2): t.rotate()
        self.assertEqual(t.getMatrice(), [[2, 2],[1, 2],[1, 1],[0, 1]])

    def test_rotateZ3(self):
        t = tetromino.Tetromino('Z')
        for i in range(0,3): t.rotate()
        self.assertEqual(t.getMatrice(), [[0, 2],[0, 1],[1, 1],[1, 0]])

    def test_rotateZ4(self):
        t = tetromino.Tetromino('Z')
        for i in range(0,4): t.rotate()
        self.assertEqual(t.getMatrice(), [[0, 0],[1, 0],[1, 1],[2, 1]])
