# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_035A import execute


class TestABC035A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(4, 3), '4:3')

    def test_execute_2(self):
        self.assertEqual(execute(16, 9), '16:9')

    def test_execute_3(self):
        self.assertEqual(execute(28, 21), '4:3')
