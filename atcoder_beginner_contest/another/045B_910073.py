# /usr/bin/env python
# coding: utf-8

# リスト内包表記を用いた辞書の初期化
S = {c: list(input()) for c in 'abc'}
s = 'a'
while S[s]:
    # 文字列をリストにして持っているのでpop()が使える
    # 文字列のままだと取り出しと対象のインデックス保持に手間が必要
    s = S[s].pop(0)
print(s.upper())
