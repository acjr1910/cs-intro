def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if not aDict:
        return None

    biggest = None
    biggest_len = 0
    for key in aDict.keys():
        key_len = len(aDict[key])
        if key_len > biggest_len:
            biggest_len = key_len
            biggest = key
    return biggest
