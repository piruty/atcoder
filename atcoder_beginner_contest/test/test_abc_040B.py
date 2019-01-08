# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_040B import execute


class TestABC040B(TestCase):

    def test_execute_(self):
        self.assertEqual(execute(26), 1)

    def test_execute_(self):
        self.assertEqual(execute(41), 4)

    def test_execute_(self):
        self.assertEqual(execute(100000), 37)
