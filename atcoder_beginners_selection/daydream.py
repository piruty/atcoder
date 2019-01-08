#! /usr/bin/env python3

s = input()

if s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '') == '':
    print('YES')
else:
    print('NO')
