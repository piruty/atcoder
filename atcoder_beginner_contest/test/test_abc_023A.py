# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_023A import execute


class TestABC023A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(23), 5)

    def test_execute_2(self):
            self.assertEqual(execute(70), 7)

    def test_execute_3(self):
            self.assertEqual(execute(99), 18)
