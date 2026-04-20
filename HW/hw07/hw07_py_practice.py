def square(n):
    return n * n


def pow_fast(base, exp):
    """Return base**exp using recursive fast exponentiation."""
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = pow_fast(base, exp // 2)
        return half * half
    return base * pow_fast(base, exp - 1)


def repeatedly_cube(n, x):
    """Cube x repeatedly n times."""
    if n == 0:
        return x
    y = repeatedly_cube(n - 1, x)
    return y * y * y


def repeatedly_cube(n, x):
    """Cube x repeatedly n times."""
    if n == 0:
        return x
    else:
        y = repeatedly_cube(n - 1, x)
        return y * y * y


def cadr(s):
    """Return the second element."""
    return s[1]


def caddr(s):
    """Return the third element."""
    return s[2]


if __name__ == "__main__":
    assert pow_fast(2, 5) == 32
    assert pow_fast(10, 3) == 1000
    assert pow_fast(3, 3) == 27
    assert pow_fast(1, 100_000_000_000_000) == 1

    assert repeatedly_cube(3, 1) == 1
    assert repeatedly_cube(2, 2) == 512
    assert repeatedly_cube(3, 2) == 134217728

    assert cadr([1, 2, 3, 4]) == 2
    assert caddr([1, 2, 3, 4]) == 3

    print("All practice tests passed!")
