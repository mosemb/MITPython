def getRatios(v1,v2):
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            ratios.append('NaN')
        except :
            raise ValueError('get rations called with bad arg')
    return ratios             
                