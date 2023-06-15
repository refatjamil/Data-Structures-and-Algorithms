def fibonacce(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2 :
        return 1
    else:   
        return fibonacce(n-2) + fibonacce(n-1)

def test():
    assert fibonacce(0) == 0
    assert fibonacce(1) == 1
    assert fibonacce(2) == 1
    assert fibonacce(3) == 2
    assert fibonacce(4) == 3  
    assert fibonacce(5) == 5    