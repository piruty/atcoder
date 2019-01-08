# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_037A import execute


class TestABC037A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, 5, 6), 2)

    def test_execute_(self):
        self.assertEqual(execute(8, 6, 20), 3)
