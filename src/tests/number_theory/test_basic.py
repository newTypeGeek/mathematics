from number_theory.basic import gcd


def test_divisible_by_gcd():
    a = 24  # 24 = 2 x 2 x 2 x 3
    b = 16  # 16 = 2 x 2 x 2 x 2
    g = gcd(a, b)
    assert a % g == 0
    assert b % g == 0


def test_gcd_of_coprime_numbers():
    a = 16
    b = 25
    assert gcd(a, b) == 1


def test_gcd_with_one_being_zero():
    x = 5
    assert gcd(0, x) == x
    assert gcd(x, 0) == x


def test_gcd_with_both_zero():
    assert gcd(0, 0) == 0


def test_gcd_is_commutative():
    a = 30624110
    b = 534202
    assert gcd(a, b) == gcd(b, a)


def test_gcd_is_associative():
    a = 30624110
    b = 534202
    c = 13942
    assert gcd(a, gcd(b, c)) == gcd(gcd(a, b), c)
