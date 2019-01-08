# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_026A import execute


class TestABC026A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(10), 25)

    def test_execute_2(self):
        self.assertEqual(execute(60), 900)
