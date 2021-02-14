def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if len(aStr) <= 1:
        return False

    half_int = int(len(aStr)/2)
    middle_char = aStr[half_int]

    if middle_char == char:
        return True
    if char < middle_char:
        return isIn(char, aStr[0:half_int])
    else:
        return isIn(char, aStr[half_int:len(aStr)])
