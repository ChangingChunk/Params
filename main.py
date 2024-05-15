values_list = [True, 101, 'Oh, hi Mark']
values_dict = {'a': 101, 'b': False, 'c': 'Mmm'}
values_list_2 = ['kek', False]

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params(False, 'Hello!')
print_params(b=25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)