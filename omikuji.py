"""
ランダムにおみくじの結果を返す
"""

import random

omikuji = ["大吉", "吉", "中吉", "末吉", "小吉", "凶", "大凶", "笑吉"]

idx = random.randint(0, len(omikuji) - 1)

print(omikuji[idx])
