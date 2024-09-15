def gcd(a: int, b: int) -> int:
    """
    Greatest Common Divisor of two integers a and b
    Here, Euclidean algorithm is used
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """
    Least Common Multiple of two integers a and b
    """
    return (a * b) / gcd(a, b)
