
def divisors( n1, n2):
    div = ()
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            div = div + (i,)
    return div , sum(div)
        
                           
            