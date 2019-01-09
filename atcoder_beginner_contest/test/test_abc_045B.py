# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_045B import execute


class TestABC045B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute({'a': 'aca', 'b': 'accc', 'c': 'ca'}), 'A')

    def test_execute_2(self):
        self.assertEqual(execute({'a': 'abcb', 'b': 'aacb', 'c': 'bccc'}), 'C')
