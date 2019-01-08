if test (count $argv) -eq 0
  echo "Plz pass problem title"
  exit 1
end

set problem $argv[1]

if test -e atcoder_beginner_contest/abc_$problem.py
  echo "$problem files already exist."
  exit 1
end

## make exec python file
printf "\
def execute(value):
    pass


if __name__ == '__main__':
    print(execute(input()))
" > atcoder_beginner_contest/abc_$problem.py

## make test python file
printf "\
# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_$problem import execute


class TestABC$problem(TestCase):

    def test_execute_(self):
        self.assertEqual(execute(), )
" > atcoder_beginner_contest/test/test_abc_$problem.py
