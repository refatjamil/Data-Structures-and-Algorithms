def bubble_sort(L):
    n = len(L)
    for i in range(0, n-1):
        sp = False
        for j in range(0, n-1-i):
            if L[j] > L[j+1]:
                L[j+1], L[j] = L[j], L[j+1]
                sp = True
        if sp is False:
            break            

if __name__ == "__main__":

    L = [9, 2, 7, 4, 5]
    print("Before sort:", L)
    bubble_sort(L) 
    print(bubble_sort(L))
    print("After sort:", L)