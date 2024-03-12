#!/usr/bin/python3
"""This script solves a game"""


def isWinner(x, nums):
    """Finding the winner of this game"""
    if x < 1 or not nums:
        return None

    marias_wins = 0
    bens_wins = 0

    n = max(nums)
    primes = [True for h in range(1, n + 1, 1)]
    primes[0] = False
    for k, is_prime in enumerate(primes, 1):
        if k == 1 or not is_prime:
            continue
        for s in range(k + k, n + 1, k):
            primes[s - 1] = False

    for p, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return 'Maria'
    elif marias_wins < bens_wins:
        return 'Ben'
