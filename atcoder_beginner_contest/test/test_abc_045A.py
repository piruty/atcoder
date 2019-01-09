# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_045B import execute


class TestABC045B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, 4, 2), 7)

    def test_execute_2(self):
        self.assertEqual(execute(4, 4, 4), 16)
