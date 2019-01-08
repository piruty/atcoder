# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_011A import execute


class TestABC011A(TestCase):
    def test_execute1(self):
        self.assertEqual(execute(1), 2)

    def test_execute2(self):
        self.assertEqual(execute(2), 3)

    def test_execute3(self):
        self.assertEqual(execute(3), 4)

    def test_execute4(self):
        self.assertEqual(execute(4), 5)

    def test_execute5(self):
        self.assertEqual(execute(5), 6)

    def test_execute6(self):
        self.assertEqual(execute(6), 7)

    def test_execute7(self):
        self.assertEqual(execute(7), 8)

    def test_execute8(self):
        self.assertEqual(execute(8), 9)

    def test_execute9(self):
        self.assertEqual(execute(9), 10)

    def test_execute10(self):
        self.assertEqual(execute(10), 11)

    def test_execute11(self):
        self.assertEqual(execute(11), 12)

    def test_execute12(self):
        self.assertEqual(execute(12), 1)
