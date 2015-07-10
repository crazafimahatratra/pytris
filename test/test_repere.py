#!/usr/bin/env python
import unittest
from tetromino import point

class TestRepere(unittest.TestCase):
    def setUp(self):
        pass

    def test_repere1(self):
        p = point.Point(0,1)
        center = point.Point(1,1)
        p.translate(center)
        self.assertEqual(p.toString(), "(-1,0)")

    def test_repere2(self):
        p = point.Point(1,0)
        center = point.Point(1,1)
        p.translate(center)
        self.assertEqual(p.toString(), "(0,-1)")

    def test_repere3(self):
        p = point.Point(0,0)
        center = point.Point(1,2)
        p.translate(center)
        self.assertEqual(p.toString(), "(-1,-2)")

    def test_repere4(self):
        p = point.Point(0,-1)
        center = point.Point(-1,-1)
        p.translate(center)
        self.assertEqual(p.toString(), "(1,0)")

    def test_inverse1(self):
        p = point.Point(1,1)
        p.inverse()
        self.assertEqual(p.toString(), "(-1,-1)")
