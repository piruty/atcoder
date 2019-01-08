# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_028A import execute


class TestABC028A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(80), 'Good')

    def test_execute_2(self):
        self.assertEqual(execute(100), 'Perfect')

    def test_execute_3(self):
        self.assertEqual(execute(59), 'Bad')

    def test_execute_4(self):
        self.assertEqual(execute(95), 'Great')
