a = list(map(int,input("enter numbers with spaces:").split()))
max1 = max2 = float('-inf')
for n in a:
    if n > max1:
        max2 = max1  
        
        
        max1 = n     
        
    
    elif n > max2 and n != max1:
      
        
        max2 = n  

print(max2)