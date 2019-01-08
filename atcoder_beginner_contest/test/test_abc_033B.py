# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_033B import execute


class TestABC033B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(4, [["unagi", 20], ["usagi", 13], ["snuke", 42], ["smeke", 7]]), 'snuke')

    def test_execute_2(self):
        self.assertEqual(execute(5, [["a", 10], ["b", 20], ["c", 30], ["d", 40], ["e", 100]]), 'atcoder')

    def test_execute_3(self):
        self.assertEqual(execute(14, [["yasuzuka", 3340], ["uragawara", 4032], ["oshima", 2249], ["maki", 2614], ["kakizaki", 11484], ["ogata", 10401], ["kubiki", 9746], ["yoshikawa", 5142], ["joetsu", 100000], ["nakago", 4733], ["itakura", 7517], ["kiyosato", 3152], ["sanwa", 6190], ["nadachi", 3169]]), 'joetsu')
