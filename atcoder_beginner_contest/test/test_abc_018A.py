# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_018A import execute


class TestABC018A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(12, 18, 11), [2, 1, 3])

    def test_execute_2(self):
        self.assertEqual(execute(10, 20, 30), [3, 2, 1])
