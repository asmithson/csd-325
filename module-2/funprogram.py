# Python program to demonstrate working
# of the filter function that filters vowels.
# Credit goes to GeeksforGeeks as program was taken from
# https://www.geeksforgeeks.org/functional-programming-in-python/

def fun(variable):
    
        letters = ['a', 'e', 'i', 'o', 'u']
        
        if (variable in letters):
            return True
        else:
            return False
        
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')

for s in filtered:
    print(s)