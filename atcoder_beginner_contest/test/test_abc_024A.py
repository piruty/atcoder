# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_024A import execute


class TestABC024A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(100, 200, 50, 20, 40, 10), 3500)

    def test_execute_2(self):
            self.assertEqual(execute(400, 1000, 400, 21, 10, 10), 14000)

    def test_execute_3(self):
            self.assertEqual(execute(400, 1000, 400, 20, 10, 10), 6000)
