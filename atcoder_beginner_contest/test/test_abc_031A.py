# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_031A import execute


class TestABC031A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(31, 87), 2784)

    def test_execute_2(self):
        self.assertEqual(execute(101, 65), 6666)

    def test_execute_3(self):
        self.assertEqual(execute(3, 3), 12)
