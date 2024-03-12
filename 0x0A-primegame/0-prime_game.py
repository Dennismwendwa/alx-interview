"""This script solves a game"""

def isWinner(x, nums):
    """This is the gamfunction"""
    def is_prime(num):
        """checks if number is prime number"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        """Generates all primes"""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def optimal_move_left(nums):
        """For player moves"""
        for prime in primes:
            if any(num % prime == 0 for num in nums):
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        """Game loop"""
        primes = get_primes_up_to_n(n)
        current_player = 'Maria'

        while optimal_move_left(nums):
            if current_player == 'Maria':
                for prime in primes:
                    if any(num % prime == 0 for num in nums):
                        nums = [num for num in nums if num % prime != 0]
                        current_player = 'Ben'
                        break
            else:
                for prime in primes:
                    if any(num % prime == 0 for num in nums):
                        nums = [num for num in nums if num % prime != 0]
                        current_player = 'Maria'
                        break

        if current_player == 'Maria':
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
