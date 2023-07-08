def recursive_binary_search(L, target,  left = None, right = None):

    if target > len(L) or target <= 0:
        return None

    if left is None and right is None:
        left = 0
        right = len(L) - 1

    mid = (left + right) // 2

    if L[mid] == target:
        return mid
    
    elif L[mid] < target:
        return recursive_binary_search(L, target, mid+1, right)
    
    else:
        return recursive_binary_search(L, target, left, mid-1)




li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('index position:',recursive_binary_search(li, 3))            