# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_021A import execute


class TestABC021A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(5), [2, 1, 4])

    def test_execute_2(self):
            self.assertEqual(execute(1), [1, 1])
