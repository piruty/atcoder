# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_011B import execute


class TestABC011B(TestCase):
    def test_execute_taKahAshI(self):
            self.assertEqual(execute('taKahAshI'), 'Takahashi')

    def test_execute_A(self):
        self.assertEqual(execute('A'), 'A')

