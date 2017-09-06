# Logic-2 Coding Bat
# Link: http://codingbat.com/python


def make_bricks(small, big, goal):
    """

    We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
    bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.
    This is a little harder than it looks and can be done without any loops.

    :param small: Int denoting number of small (1 inch) bricks
    :param big: Int denoting number of big (5 inch) bricks
    :param goal: Int denoting the goal
    :return: True or False as to whether the goal can be reached with the given bricks
    """

    # Divide and Conquer: Handle all possible fail cases

    # Case 1: Not enough bricks
    if goal - (big * 5) - small > 0:
        return False

    # Case 2: Not enough small bricks
    # Note: Case 1 checks if there are enough bricks, so it is given that there are either enough small, enough big,
    # or some sort of combination thereof
    if goal % 5 > small:
        return False

    return True


def lone_sum(a, b, c):
    """

    Given 3 int values, a b c, return their sum.
    However, if one of the values is the same as another of the values, it does not count towards the sum.

    :param a: Int
    :param b: Int
    :param c: Int
    :return: Sum of unique values in a, b, c
    """

    # noinspection PyTypeChecker
    return sum(x for x in [a, b, c] if [a, b, c].count(x) == 1)


def lucky_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if one of the values is 13 then
    it does not count towards the sum and values to its right do not count. So for example,
    if b is 13, then both b and c do not count.

    :param a: Int
    :param b: Int
    :param c: Int
    :return: Int
    """
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c


# Helper Method for no_teen_sum(a,b,c)
def fix_teen(n):
    if n in range(13, 20) and n not in range(15, 17):
        n = 0
    return n


def no_teen_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if any of the values is a teen --
    in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count
    as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns
    that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times
    (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

    :param a: Int
    :param b: Int
    :param c: Int
    :return: Int
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def round10(num):
    if num % 10 < 5:
        num = num - (num % 10)
        return num
    num = num + (10 - num % 10)
    return num


def round_sum(a, b, c):
    """
    For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
    so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less
    than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values.
    To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
    Write the helper entirely below and at the same indent level as round_sum().

    :param a: Int
    :param b: Int
    :param c: Int
    :return: Int
    """
    return round10(a) + round10(b) + round10(c)


def close_far(a, b, c):
    """

    :param a: Int
    :param b: Int
    :param c: Int
    :return: Bool
    """
    if abs(a - b) <= 1:
        return abs(c - a) >= 2 and abs(c - b) >= 2
    if abs(a - c) <= 1:
        return abs(b - a) >= 2 and abs(b - c) >= 2


def make_chocolate(small, big, goal):
    """
    We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
    Return the number of small bars to use, assuming we always use big bars before small bars.
    Return -1 if it can't be done.

    :param small: number of small bars valued at 1 kilo each
    :param big: number of big bars valued at 5 kilos each
    :param goal: total number of kilos needed to package
    :return: -1 , used as a bool value
    """
    # failure case 1: not enough bars
    if goal > big * 5 + small:
        return -1

    # failure case 2: not enough small or big
    if goal < big * 5 and goal % 5 > small:
        return -1

    if goal < big * 5:
        return goal % 5
    return goal - big * 5
