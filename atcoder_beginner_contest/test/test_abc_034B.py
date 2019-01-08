# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_034B import execute


class TestABC034B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(100), 99)

    def test_execute_2(self):
        self.assertEqual(execute(123456789), 123456790)
