List = [9, 2, 7, 4, 5]

Lenth_of_List = len(List)
for j in range(0,Lenth_of_List):
    swap =   False
    for i in range(0,Lenth_of_List-j-1):
        if List[i] > List[i+1]:
            List[i],List[i+1] = List[i+1], List[i]
            swap = True
    if swap != True:        
        break        

print(List)
