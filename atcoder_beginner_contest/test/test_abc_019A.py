# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_019A import execute


class TestABC019A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(2, 3, 4), 3)

    def test_execute_2(self):
            self.assertEqual(execute(5, 100, 5), 5)

    def test_execute_3(self):
            self.assertEqual(execute(3, 3, 3), 3)

    def test_execute_4(self):
            self.assertEqual(execute(3, 3, 4), 3)
