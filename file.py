# doctests are simple blackbox (not unit) tests that show what the expected
# return value from a function should be.
#
# To write a doctest, add a heredoc comment to inside of a function and write
# any necessary comments about that code / logic (below, see "Basic sanity test")
# The test it's self is the invocation of the function (plus_one(2)) and the
# assertion following on the next line (3).
#
# Running doc tests are fairly straightforward using the __main__ method
# like shown below, just run python FILE_NAME.py
# Output isn't shown if the tests run successfully but failures appear like below.
#
# **********************************************************************
# File "file.py", line 43, in __main__.return_true
# Failed example:
#     return_true()
# Expected:
#     False
# Got:
#     True
# **********************************************************************
# 1 items had failures:
#    1 of   2 in __main__.return_true
# ***Test Failed*** 1 failures.
#
def plus_one(n):
    """
    Basic sanity test

    >>> plus_one(2)
    3

    >>> plus_one(-12)
    Traceback (most recent call last):
    ...
    Exception: Can't have negative numbers!

    """
    if n < 0:
        raise Exception("Can't have negative numbers!")
    return n + 1


def return_true():
    """
    >>> return_true()
    True

    A sample broken test to demo failure
    >>> return_true()
    False
    """


    return True

if __name__ == "__main__":
    import doctest
    # kwarg raise_on_error=True is required to make doc tests return a non 0 status code on failure.
    # This wouldn't matter to the students much, but would matter if we want to use a CI server.
    doctest.testmod()
