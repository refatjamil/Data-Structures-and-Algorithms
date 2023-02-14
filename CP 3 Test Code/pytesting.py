def avg(L):
    if not L:
        return None
    return sum(L)/len(L)
        

L = [1, 2, 3, 4, 5]

expected_result = 3.0

def test_avg():
    assert expected_result == avg(L)
