# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_ccc import execute


class TestABC012(TestCase):

    def test_execute_1(self):
        self.assertEqual(6, execute([1, 3, -3]))

    def test_execute_2(self):
        self.assertEqual(4, execute([4, 3, 2, 5, 1, 1]))

    def test_execute_3(self):
        self.assertEqual(0, execute([1] * 100000))

    def test_execute_4(self):
        self.assertEqual(3, execute([1, 3, -3, 4, 4]))

    def test_execute_5(self):
        self.assertEqual(1, execute([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]))

    def test_execute_6(self):
        self.assertEqual(5, execute([9, 8, 3, 10, 1, 2, 3, 10, 5]))

    def test_execute_7(self):
        self.assertEqual(5, execute([5, 10, 3, 2, 1, 10, 3, 8, 9]))

    def test_execute_8(self):
        self.assertEqual(2, execute([4, 3, 2, 5, 3]))
