def falling(n, k):
    """ To check the factorial n!

        >>> falling(7,2)
        42
        >>> falling(8,0)
        1
        >>> falling(4,3)
        24
    """
    if n < k:
        return "k should be less than n!"
    elif n == 1:
        return 1
    elif k == 0:
        return 1
    elif (n > 0 and k > 0):
        count = 1
        tmp = n -1
        while count < k:
            n, tmp = n * tmp, tmp - 1
            count += 1
        return n