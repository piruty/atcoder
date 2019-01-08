# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_015A import execute


class TestABC015A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute('isuruu', 'isleapyear'), 'isleapyear')

    def test_execute_2(self):
        self.assertEqual(execute('ttttiiiimmmmeeee', 'time'), 'ttttiiiimmmmeeee')
