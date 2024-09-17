import pytest

from number_theory.prime_factors import brute_force_prime_factors


def test_prime_factorisation():
    n = 11 * 17 * 41
    prime_factors = brute_force_prime_factors(n)
    assert prime_factors == [11, 17, 41]


def test_for_two():
    n = 2
    prime_factors = brute_force_prime_factors(n)
    assert prime_factors == [2]


def test_for_one_raises_assertion_error():
    n = 1
    with pytest.raises(AssertionError):
        brute_force_prime_factors(n)
