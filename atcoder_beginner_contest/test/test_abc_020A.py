# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_020A import execute


class TestABC020A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(1), 'ABC')

    def test_execute_2(self):
            self.assertEqual(execute(2), 'chokudai')
