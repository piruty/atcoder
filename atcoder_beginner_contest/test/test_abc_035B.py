# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_035B import execute


class TestABC035B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('UL?', 1), 3)

    def test_execute_2(self):
        self.assertEqual(execute('UD?', 1), 1)

    def test_execute_3(self):
        self.assertEqual(execute('UUUU?DDR?LLLL',  1), 7)

    def test_execute_4(self):
        self.assertEqual(execute('UULL?', 2), 3)
