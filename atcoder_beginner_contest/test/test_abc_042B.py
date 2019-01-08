# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_042B import execute


class TestABC042B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, 3, ['dxx', 'axx', 'cxx']), 'axxcxxdxx')
