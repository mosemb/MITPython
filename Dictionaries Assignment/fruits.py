str1 = 'AC'
ditn = {'A':1, 'B':2, 'C':3}
list1 = []

for k in str1:
    if True:
        list1.append(k)

for i, j in enumerate(str1):
    if list1[0] in ditn.keys():
        ditn[list1[0]]= ditn[list1[0]]-1
        list1.pop(0)
    else:
        ditn[list1[i]]=ditn[list1[i]]+1
    print ditn   
    
for ik, g  in enumerate( list1):
    if list1[ik] != str1[0]:
        ditn[g]= ditn[g]+1
    if list1[ik]==str1[-1::]:
        ditn[g]=ditn[g]
    print list1
            
    #print ditn , ditn[g] 
      
for im in ditn.keys():
    if im not in list1:
        ditn[im]=ditn[im]+1
    print ditn                                 
    
    
    
    #if list1[ik] in ditn.keys() or not in ditn.keys():    