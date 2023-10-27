

def countDigits(x): 
    if x < 10:
         return 1 
    else: 
        return 1 + countDigits(x // 10) # recursive that divide x by 10 (to remove the last digit) and add 1 to the result
        
        
