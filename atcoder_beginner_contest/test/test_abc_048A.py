# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_048A import execute


class TestABC048A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute("AtCoder Beginner Contest"), "ABC")

    def test_execute_2(self):
        self.assertEqual(execute("AtCoder Snuke Contest"), "ASC")

    def test_execute_3(self):
        self.assertEqual(execute("AtCoder X Contest"), "AXC")
