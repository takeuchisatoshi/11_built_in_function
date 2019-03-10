"""
ランダムにおみくじの結果を返す
"""

import random

omikuji = ["大大吉", "大吉", "凶後大吉", "凶後吉", "末大吉", "末吉", "向大吉", "吉", "中吉", "小吉", "小凶後吉", "後吉", "吉凶未分末大吉", "吉凶不分末吉", "吉凶相半", "吉凶相交末吉", "吉凶相央"]

# print(len(omikuji))

"""
伏見稲荷大社 式
大大吉・大吉・凶後大吉・凶後吉・末大吉・末吉・向大吉・吉・中吉・小吉・小凶後吉・後吉・吉凶未分末大吉・吉凶不分末吉・吉凶相半・吉凶相交末吉・吉凶相央

置換は Edit > Find > Replace
command + R
"""

# idx = random.randint(0, len(omikuji) - 1)
#
# print(omikuji[idx])

print(random.choice(omikuji))
