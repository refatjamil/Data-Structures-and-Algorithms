def fibonacce(n):
    if  n == 1 or n == 2:
        return 1
    return fibonacce(n-2) + fibonacce(n-1)

def test():
    fib = [1,1,2,3,5,8,13,21,34,55,89]
    for i, f in enumerate(fib):
        assert fibonacce(i+1) == f