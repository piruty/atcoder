# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_027A import execute


class TestABC027A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute([1, 1, 2]), 2)

    def test_execute_2(self):
        self.assertEqual(execute([4, 3, 4]), 3)

    def test_execute_3(self):
        self.assertEqual(execute([5, 5, 5]), 5)
