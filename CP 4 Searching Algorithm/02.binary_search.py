def binary_search(List, Tergat):
    left_index_number = 0
    right_index_number = len(List) -1

    while left_index_number <= right_index_number:
        mid_index_number = (right_index_number + right_index_number) // 2

        if List[mid_index_number] == Tergat:
            return mid_index_number
        
        if List[mid_index_number] < Tergat:
            left_index_number = mid_index_number + 1
        else:
            right_index_number = mid_index_number -1
    return -1

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in range(len(L)):
        position = binary_search(L, x)

        if position == -1:
            if x in L:
                print(x, "is in L, but function returned -1")
            else:
                print(x, "not in list")
        else:
            if L[position] == x:
                print(x, "found in correct position")
            else:
                print("binary search in returned", position, "for", x, "which is incorrect")
    print("program terminated")                
