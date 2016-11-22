numcons=0
numvol = 0
school = ("Massachusetts Institute of Technology")
for char in school:
    if char!='a'and char!='e'and char!='i'and char!='o'and char!='u':
        numcons = numcons+1
    elif char=='a'or char=='e'or char=='i'or char=='o'or char=='u':
        numvol = numvol+1
        
print str(numcons)
print str(numvol)
print len(school)
        