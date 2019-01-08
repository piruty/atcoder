# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_036A import execute


class TestABC036A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(12, 36), 3)

    def test_execute_2(self):
        self.assertEqual(execute(12, 100), 9)
