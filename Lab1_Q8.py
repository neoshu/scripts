def double_eights(n):
    """Return true if n has two eights in a row.

    """
    if n < 88:
        return False
    else:
        str_n = str(n)
        pos = 0
        while pos < len(str_n):
            if (str_n[pos] == "8" and str_n[pos+1] == "8"):
                return True
            pos += 1
        return False