
def plus_one(n):
    """
    Test derp

    >>> plus_one(2)
    3

    >>> plus_one(-12)
    Traceback (most recent call last):
    ...
    Exception: Can't have negative numbers!

    """
    if n < 0:
        raise Exception("Can't have negative numbers!")
    return n+1


def return_true():
    """
    >> return_true()
    True

    """

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(raise_on_error=True)
