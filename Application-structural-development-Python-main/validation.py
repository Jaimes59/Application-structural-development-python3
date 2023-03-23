def is_int(value):
    """
    Function that checks if the value is an integer.
    :param value:
    :type value: int
    :returns: True if object is int, False otherwise,
    :rtype: bool
    """
    return isinstance(value, int)


def is_greater_than_zero(value):
    """
    Function that checks if a number is greater than zero.
    :param value: number to check.
    :type value: int or float
    :returns: True if number is greater than zero, False otherwise.
    :rtype: bool
    """
    return value > 0
