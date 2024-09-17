def brute_force_prime_factors(n: int) -> list[int]:
    prime_factors = []

    # prime factor candidates 2, 3, ..., n
    for i in range(2, n + 1):

        # if i no longer divisble by n, then we iterate to the next i
        # we don't need to check for i being prime, as we start from 2 which is prime
        # let say composite number 4 is a factor or n, then its previous i = 2 is also a factor of n
        # so it should already be extracted
        while n % i == 0:
            # divisble means i is a (prime) factor of n
            prime_factors.append(i)

            # update the value of n as we extracted the prime factor i
            n //= i

    return prime_factors
