# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_029B import execute


class TestABC029B(TestCase):

    def test_execute_1(self):
        params = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december',]
        self.assertEqual(execute(params), 8)

    def test_execute_2(self):
        params = ['rrrrrrrrrr', 'srrrrrrrrr', 'rsr', 'ssr', 'rrs', 'srsrrrrrr', 'rssrrrrrr', 'sss', 'rrr', 'srr', 'rsrrrrrrrr', 'ssrrrrrrrr']
        self.assertEqual(execute(params), 11)
