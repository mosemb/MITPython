def items_order(order):
    countsalad = order.count("salad")
    counthumberger= order.count("humberger")
    countwater = order.count("water")
    
    return 'salad:'+ str(countsalad) + ' humberger:'+ str(counthumberger) + ' water:' + str( countwater) 
    
   
     