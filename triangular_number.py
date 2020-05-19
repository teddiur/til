"""
A triangular number is the product of three sequential natural numbers
"""

def is_triangular(n):
    for m in range(int(n)//2):
        if m*(m+1)*(m+2) == int(n):
            print('É triangular')
            return True
        elif m*(m+1)*(m+2) > int(n):
            print('Não é triangular')
            return False

number = input('Enter a number to check if it\'s triangular: ')
is_triangular(number)