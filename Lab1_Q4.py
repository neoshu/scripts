def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    count = 0
    if n < k:
        return count
    elif n == 0:
        return "N/A"
    else:
        can_be_divided = 1
        while can_be_divided <= n:
            if can_be_divided % k == 0:
                print(can_be_divided)
                count += 1
            can_be_divided += 1
        return count