#!/usr/bin/python3
"""Prime Game"""


def isWinner(num_rounds, rounds):
    """Determine the winner of each round of the Prime Game"""
    if not rounds or num_rounds < 1:
        return None

    max_round = max(rounds)

    # Create a list to check if a number is prime
    prime_check = [True for _ in range(max(max_round + 1, 2))]

    # Sieve of Eratosthenes to find all primes up to max_round
    for i in range(2, int(pow(max_round, 0.5)) + 1):
        if not prime_check[i]:
            continue
        for j in range(i * i, max_round + 1, i):
            prime_check[j] = False

    prime_check[0] = prime_check[1] = False

    # Count the number of primes up to each number
    prime_counts = [0]
    for i in range(1, len(prime_check)):
        prime_counts.append(prime_counts[i-1] + int(prime_check[i]))

    # Determine the winner of each round
    Maria_wins = sum(prime_counts[n] % 2 for n in rounds)

    if Maria_wins * 2 == num_rounds:
        return None
    elif Maria_wins * 2 > num_rounds:
        return "Maria"
    else:
        return "Ben"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, -1, 0])))
