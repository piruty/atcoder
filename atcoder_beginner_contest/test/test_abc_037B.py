# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_037B import execute


class TestABC037B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(5, 2, [[1, 3, 10], [2, 4, 20]]), '10\n20\n20\n20\n0')

    def test_execute_2(self):
        self.assertEqual(execute(10, 4, [[2, 7, 22], [3, 5, 4], [6, 10, 1], [4, 4, 12]]), '0\n22\n4\n12\n4\n1\n1\n1\n1\n1')


