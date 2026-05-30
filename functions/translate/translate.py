def translate(object= str ,origin=list, destination=list):
    """find a object that have a same index in anither list

    Args:
        object (str):
        origin (list): a list that we have the object
        destination (list): a list that we want to find the same indexed object
    Return:
        str: a object with same index in destination list"""
    try:
        n = destination[origin.index(object)]
    except :
        n = ''
    return n
