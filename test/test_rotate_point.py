#!/usr/bin/env python
import unittest
from tetromino import point

class TestRotatePoint(unittest.TestCase):
    def setUp(self):
        pass

    def test_rotate0(self):
        p = point.Point(1,0)
        center = point.Point(0,0)
        p.rotate(center)
        self.assertEqual(p.toString(), "(0,1)")

    def test_rotate1(self):
        p = point.Point(0,-1)
        center = point.Point(0,0)
        p.rotate(center)
        self.assertEqual(p.toString(), "(1,0)")

    def test_rotate2(self):
        p = point.Point(0,1)
        center = point.Point(1,1)
        p.rotate(center)
        self.assertEqual(p.toString(), "(1,0)")

    def test_rotate3(self):
        p = point.Point(1,0)
        center = point.Point(1,1)
        p.rotate(center)
        self.assertEqual(p.toString(), "(2,1)")

    def test_rotate4(self):
        p = point.Point(0,0)
        center = point.Point(1,2)
        p.rotate(center)
        self.assertEqual(p.toString(), "(3,1)")

    def test_rotate5(self):
        p = point.Point(-1,1)
        p.rotateBy90()
        self.assertEqual(p.toString(), "(-1,-1)")

    def test_rotate6(self):
        p = point.Point(0,0)
        center = point.Point(1,1)
        p.translateByCenter(center)
        self.assertEqual(p.toString(), "(-1,-1)")
        p.rotateBy90()
        self.assertEqual(p.toString(), "(1,-1)")
        p.backFromTranslation(center)
        self.assertEqual(p.toString(), "(2,0)")

    def test_rotate7(self):
        p = point.Point(0,1)
        center = point.Point(1,1)
        p.translateByCenter(center)
        self.assertEqual(p.toString(), "(-1,0)")
        p.rotateBy90()
        self.assertEqual(p.toString(), "(0,-1)")
        p.backFromTranslation(center)
        self.assertEqual(p.toString(), "(1,0)")

    def test_rotate8(self):
        p = point.Point(0,1)
        center = point.Point(1,1)
        p.rotate(center)
        self.assertEqual(p.toString(), "(1,0)")

    def test_rotate9(self):
        p = point.Point(2,1)
        center = point.Point(1,1)
        p.rotate(center)
        self.assertEqual(p.toString(), "(1,2)")
