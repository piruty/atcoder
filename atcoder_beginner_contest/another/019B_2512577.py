# https://beta.atcoder.jp/contests/abc019/submissions/2512577

import re
print(re.sub(r'(.)\1*', lambda x: x.group(1) + str(len(x.group(0))), input()))
