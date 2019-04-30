# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_ddd import execute


class TestABCddd(TestCase):

    def test_execute_1(self):
        self.assertEqual(3, execute([2, 1, 1, 3, 2, 1, 1, 3]))

    def test_execute_2(self):
        self.assertEqual(6, execute([7, 5, 2, 7, 2, 7, 4, 7]))

    def test_execute_3(self):
        self.assertEqual(1, execute([7] * 100000))
