def avg(L):
    if not L:
        return None
    return sum(L)/len(L)
        

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]

    expected_result = 3.0
    result = avg(L)

    if expected_result == result:
        print("test passed")
    else:
        print(f"test failes! output: {result} expected: {expected_result}")    
