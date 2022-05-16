new_list = [1, 2, 3, 4, 5] # creat list/array
print(new_list)


result1 = new_list[0] # access index 0 
print(result1) # we found 1 on index 0 


# result2 = new_list[7] # access index 7
# print(result2) # IndexError: list index(index 7) out of range


new_list.insert(2,10) # insert(index position= 2, insert element= 10)
print(new_list) # list changed [1, 2, 3, 4, 5] to [1, 2, 10, 3, 4, 5] 


new_list.append(11) # append(append element= 11) # 11 appending at end of the list.
print(new_list) # list changed [1, 2, 10, 3, 4, 5] to [1, 2, 10, 3, 4, 5, 11]

new_list_2 = [12, 13, 14, 15, 16] # creat another list/array
new_list.extend(new_list_2) # extend(another list= new_list_2) #appdend another list at end of the list.
print(new_list)

