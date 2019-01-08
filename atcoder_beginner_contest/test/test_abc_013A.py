# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_013A import execute


class TestABC013A(TestCase):
    def test_execute_A(self):
        self.assertEqual(execute('A'), 1)

    def test_execute_B(self):
        self.assertEqual(execute('B'), 2)

    def test_execute_C(self):
        self.assertEqual(execute('C'), 3)

    def test_execute_D(self):
        self.assertEqual(execute('D'), 4)

    def test_execute_E(self):
        self.assertEqual(execute('E'), 5)

