def print_number_asd(n):
    if n == 0:
        return
    
    print_number_asd(n-1) 
    print(n)

print('Asending Order')
print_number_asd(5)

def print_number_desd(n):
    if n == 0:
        return
    
    print(n)
    print_number_desd(n-1)

print('Desending Order')   
print_number_desd(3)


