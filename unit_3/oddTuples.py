def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    odds = tuple()
    index = 0
    for item in aTup:
        if index % 2 == 0:
            odds = odds + (aTup[index],)
        index += 1
    return odds


oddTuples(('I', 'am', 'a', 'test', 'tuple'))
