def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divisible_by_both = 1
    gcd = 1
    smaller_int = a

    if b < a:
        smaller_int = b

    while smaller_int > 0:
        if ((a % smaller_int == 0) and (b % smaller_int == 0)):
            if (smaller_int > gcd):
                gcd = smaller_int
        smaller_int -= 1
    return gcd
