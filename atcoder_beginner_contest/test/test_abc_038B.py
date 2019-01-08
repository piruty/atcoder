# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_038B import execute


class TestABC038B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute([1080, 1920], [1080, 1920]), 'YES')

    def test_execute_2(self):
        self.assertEqual(execute([1080, 1920], [1920, 1080]), 'YES')

    def test_execute_3(self):
        self.assertEqual(execute([334, 668], [668, 1002]), 'YES')

    def test_execute_4(self):
        self.assertEqual(execute([100, 200], [300, 150]), 'NO')

    def test_execute_5(self):
        self.assertEqual(execute([120, 120], [240, 240]), 'NO')
