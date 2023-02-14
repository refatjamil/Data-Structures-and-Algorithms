def avg(L):
    if not L:
        return None
    return sum(L)/len(L)
        

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]

    expected_result = 3.2
    
    assert expected_result == avg(L), "avg() produced incorrect result"
