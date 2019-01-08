# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_024B import execute


class TestABC024B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(5, 10, [20, 100, 105, 217, 314]), 45)

    def test_execute_2(self):
            self.assertEqual(execute(10, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 19)

    def test_execute_3(self):
            self.assertEqual(execute(10, 100000, [3 , 31 , 314 , 3141 , 31415 , 314159 , 400000 , 410000 , 500000 , 777777]), 517253)
