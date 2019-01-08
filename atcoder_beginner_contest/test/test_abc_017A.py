# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_017A import execute


class TestABC017A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute([[50, 7], [40, 8], [30, 9]]), 94)

    def test_execute_2(self):
        self.assertEqual(execute([[990, 10], [990, 10], [990, 10]]), 2970)
