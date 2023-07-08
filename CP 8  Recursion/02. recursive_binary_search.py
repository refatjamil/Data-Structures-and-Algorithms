def recursive_binary_search(list, terget):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == terget:
            return True
        else:
            if list[midpoint] < terget:
                return recursive_binary_search(list[midpoint+1:],terget)
            else:
                return recursive_binary_search(list[:midpoint], terget)
            



li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('index position:',recursive_binary_search(li, 44))