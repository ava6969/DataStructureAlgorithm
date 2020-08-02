def sqrt(n, eps=0.000001):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # We are using n itself as
    # initial approximation This
    # can definitely be improved
    x = n
    y = 1
    t = 0
    while (x - y > eps):
        t += 1
        x = (x + y) // 2
        y = n / x

    return x


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (25 == sqrt(625)) else "Fail")