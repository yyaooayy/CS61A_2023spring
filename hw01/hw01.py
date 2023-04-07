from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return min(i, j, k)**2 + (i+j+k-max(i, j, k)-min(i, j, k))**2


def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    # largest_factors = 1
    # for i in range(2,int(n/2)):
    #     if n % i == 0:
    #         if largest_factors < int(n / i):
    #             largest_factors = int(n / i)
    # return largest_factors
    counter = n - 1
    while counter:
        counter -= 1
        if n % counter == 0:
            return counter


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    # i = n
    # b = 0
    # if i != 1:
    #     while i:
    #         if i % 2 == 0:
    #             a = i / 2
    #             print(a)
    #             i = a
    #             b +=1
    #         else:
    #             a = i * 3 + 1
    #             print(a)
    #             i = a
    #             b +=1
    # else:
    #     print(i)
    # return b
    counter1 = n
    print(counter1)
    counter2 = 1
    while counter1-1:
        if counter1 % 2 == 0:
            counter1 = counter1 // 2
            print(counter1)
            counter2 += 1
        else:
            counter1 = counter1 * 3 + 1
            print(counter1)
            counter2 += 1
    return counter2
