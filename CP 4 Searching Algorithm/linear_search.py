# while loop
def linear_search(L, x):
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i

        i += 1

    i = -1

    return i         


# for loop
def linear_search2(L, x):
    n = len(L)
    i = 0

    for i in range(n):
        if L[i] == x:
            return i

    return "Not Found"   


li = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18, 19, 20]    
print(linear_search2(li, 10))