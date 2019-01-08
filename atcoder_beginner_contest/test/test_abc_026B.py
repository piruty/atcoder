# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_026B import execute


class TestABC026B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, [1, 2, 3]), 18.8495559215)

    def test_execute_2(self):
        self.assertEqual(execute(6, [15, 2, 3, 7, 6, 9]), 508.938009881546)
