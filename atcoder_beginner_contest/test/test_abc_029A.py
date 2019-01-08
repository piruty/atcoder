# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_029A import execute


class TestABC029A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('dog'), 'dogs')

    def test_execute_2(self):
        self.assertEqual(execute('chokudai'), 'chokudais')
