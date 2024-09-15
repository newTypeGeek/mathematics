def greatest_common_divisor(a: int, b: int) -> int:
    # euclid algorithm
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
