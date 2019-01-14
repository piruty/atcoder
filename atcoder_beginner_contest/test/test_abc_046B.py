# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_046B import execute


class TestABC046B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(2, 2), 2)

    def test_execute_2(self):
        self.assertEqual(execute(1, 10), 10)

    def test_execute_3(self):
        self.assertEqual(execute(10, 8), 322828856)
