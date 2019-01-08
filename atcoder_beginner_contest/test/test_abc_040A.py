# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_040A import execute


class TestABC040A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(5, 2), 1)

    def test_execute_2(self):
        self.assertEqual(execute(6, 4), 2)

    def test_execute_3(self):
        self.assertEqual(execute(90, 30), 29)
