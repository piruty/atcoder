# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_027B import execute


class TestABC027B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, [1, 2, 3]), 2)

    def test_execute_2(self):
        self.assertEqual(execute(5, [2, 0, 0, 0, 3]), 3)

    def test_execute_3(self):
        self.assertEqual(execute(2, [0, 99]), -1)

    def test_execute_4(self):
        self.assertEqual(execute(4, [0, 0, 0, 0]), 0)
