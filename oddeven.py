l=list(map(int,input("enter no").split()))
el=[]
od=[]
for i in l:
    if i%2==0:
        el.append(i)
    else:
        od.append(i)
print("odd list:",od)
print("even:",el)
        
