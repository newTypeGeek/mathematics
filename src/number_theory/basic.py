def gcd(a: int, b: int) -> int:
    """
    Greatest Common Divisor of two integers a and b
    """
    if b == 0:
        return a
    return gcd(b, a % b)
