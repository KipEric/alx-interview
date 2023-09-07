#!/usr/bin/python3
"""Prime Game"""

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes(n):
    """Returns a list of prime numbers from 2 to n."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def play_round(n):
    """Simulates a round of the game and returns the winner."""
    nums = set(range(1, n + 1))
    primes = get_primes(n)
    player = 0
    while primes:
        prime = primes.pop(0)
        nums -= set(range(prime, n + 1, prime))
        player = 1 - player
        primes = [x for x in primes if x in nums]
    return player

def isWinner(x, nums):
    """Determine the winner of the Prime Game"""
    if not nums:
        return None

    score = [0, 0]
    for n in nums:
        winner = play_round(n)
        score[winner] += 1
    if score[0] > score[1]:
        return "Maria"
    elif score[1] > score[0]:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
