# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_051A import execute


class TestABC051A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('happy,newyear,enjoy'), 'happy newyear enjoy')

    def test_execute_2(self):
        self.assertEqual(execute('haiku,atcoder,tasks'), 'haiku atcoder tasks')
