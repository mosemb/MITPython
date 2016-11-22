def getSubjectstats(subject,weights):
    return [[elt[0], elt[1], avg(elt[1], weights)] 
            for elt in subject]
    
def dotproduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result +=a[i]*b[i]
    return result 
    
def avg(grades, weights):
    try:
        return dotproduct(grades, weights/len(grades)) 
    except ZeroDivisionError:
        print 'Division by zero'
        return 0.0
    except TypeError:
        newgr = [gradeconversion(elt) for elt in grades]
        return dotproduct(newgr,weights/len(newgr))    
        
def gradeconversion(grade):
    if type(grade) == int:
        return grade
    elif grade == 'A':
        return 90.0
    elif grade == 'B':
        return 80.0
    elif grade == 'C':
        return 70.0
    elif grade =='D':
        return 60
    else:
        return 50
        
                                                                                                                          
          
    