# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_012B import execute


class TestABC012B(TestCase):
    def test_execute3661(self):
        self.assertEqual(execute(3661), '01:01:01')

    def test_execute86399(self):
        self.assertEqual(execute(86399), '23:59:59')
