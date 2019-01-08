# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_039B import execute


class TestABC039B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(1), 1)

    def test_execute_2(self):
        self.assertEqual(execute(981506241), 177)

    def test_execute_3(self):
        self.assertEqual(execute(390625), 25)
