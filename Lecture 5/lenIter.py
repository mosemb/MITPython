def lenIter(aStr):
    count = 0
    for i in aStr:
        if i in "abcdefghijklmnokqrstuvwxyz" or "ABCDEFGHIJKLMNOPQRST":
            count +=1
    return count         