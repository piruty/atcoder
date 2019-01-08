# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_036B import execute


class TestABC036B(TestCase):

    def test_execute_(self):
        self.assertEqual(execute(4, [list('ooxx'), list('xoox'), list('xxxx'), list('xxxx')]), 'xxxo\nxxoo\nxxox\nxxxx')


