def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values_sum = 0
    for value in aDict.values():
        values_sum += len(value)
    return values_sum
