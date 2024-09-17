
def brute_force_prime_factors(n: int) -> list[int]:
    prime_factors = []

    # prime factor candidates 2, 3, ..., n
    for i in range(2, n + 1):
        
        # divisble means i is a (prime) factor of n
        # we don't need to check for i being prime, as we start from 2 which is prime
        while n % i == 0:
            prime_factors.append(i)

            # update the value of n as we extracted the prime factor i
            n //= i

    return prime_factors