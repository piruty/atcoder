# /usr/bin/env python
# coding: utf-8

# https://beta.atcoder.jp/contests/abc017/submissions/3384332
import re
print('NO' if re.sub('ch|o|k|u', '', input()) else 'YES')
# pythonでは空文字でない場合はTrue判定
# 正規表現で置き換えた結果、文字が残っていたらNOを返す（= choku語ではない）

