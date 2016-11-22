balance = 4213
annual_interest = 0.2
minimum_payment = 0.04*balance
new_balance = balance -minimum_payment



#New_balance =  balance - (minimum_payment*balance)
#New_balance_interest = New_balance*(annual_interest/12.0)
#New_balance_plus_interest = New_balance_interest + New_balance
for i in range(1,13):
   
        
         
    interest = round((0.2/12.0)*new_balance,2)
    real_balance = round(new_balance + interest,2)
    new_balance = round(real_balance - minimum_payment,2)
    print i, new_balance , interest , round(real_balance,2)
    

    
    
    

         
     
    
    #balance = updated_balance + (updated_balance*annual_interest)
    #if balance>0:
     #   minimum_payment += (2/100.0)*balance
    #else:
      #  break 4044.48
             
    
    
    
    


#for i in range(1,13):
   # New_balance -=  balance - (minimum_payment*balance)
   # print New_balance

