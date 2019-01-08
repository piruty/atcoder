# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_022B import execute


class TestABC022B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute([1, 2, 3, 2, 1]), 2)

    def test_execute_2(self):
            self.assertEqual(execute([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), 4)
