# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_015B import execute


class TestABC015B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(4, [0, 1, 3, 8]), 4)

    def test_execute_2(self):
        self.assertEqual(execute(5, [1, 4, 9, 10, 15]), 8)

