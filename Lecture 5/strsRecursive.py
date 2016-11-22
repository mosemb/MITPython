def strs(strings,char):
    mid = len(strings)/2
    
    char_index = strings.find(char)
    sub_string = strings[:mid]
    sub_first = strings[mid-1:mid]
    char_value = ord(char)
    int_to_char = chr(char_value)
    
    if len(strings)==1:
        return strings == char
        
    if strings == '':
       return False 
       
    if char == sub_first:
        return True
        
    elif char < sub_first:
        return strs(strings[:mid], char)
    
    else: 
        return strs(strings[mid+1:], char)                  
            
        