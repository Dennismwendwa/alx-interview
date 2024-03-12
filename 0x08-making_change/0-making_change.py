#!/usr/bin/python3
"""Analyzing the time and space complexity of algorithms"""


def makeChange(coins, total):
    """
    greedy algorithms and scenarios where they might not
    provide the optimal solution
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = []

    for coin in coins:
        count = total // coin

        coin_count.append(count)
        total = total % coin
        if total <= 0:
            break

    if total > 0:
        return -1

    return sum(coin_count)

print(int(makeChange([14, 13, 12, 4], 30)))
