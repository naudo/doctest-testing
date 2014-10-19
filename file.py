
def plus_one(n):
    """
    Test derp

    >>> plus_one(2)
    3

    >>> plus_one(-12)
    Traceback (most recent call last):
    ...
    Exception: BREAK!!!!

    """
    if n < 0:
        raise Exception("BREAK!!!!")
    return n+1


def return_true():
    """
    >> return_true()
    True

    This is a broken test to see if codeship will report a failing doctest

    >>> return_true()
    False



    """

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(raise_on_error=True)
