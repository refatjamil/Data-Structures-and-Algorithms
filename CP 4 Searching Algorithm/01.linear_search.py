# linear search with while looop
def linear_search(List, Terget):

    Lenth_of_List = len(List)
    Index_Number = 0

    while Index_Number < Lenth_of_List:
        if List[Index_Number] == Terget:
            return f"Terget Number {Terget} Index_Number: {Index_Number}"
        else:
            Index_Number = Index_Number + 1
            
    return "Terget Number Not Found"    


# with for loop
def linear_search2(L, x):
    n = len(L)
    i = 0

    for i in range(n):
        if L[i] == x:
            return i

    return "Not Found"   

if __name__ == "__main__":

    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(linear_search(L, 20))
    print(linear_search2(L, 10))