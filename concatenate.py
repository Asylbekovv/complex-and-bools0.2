int_num = 44
float_num = 4.8
print(float_num.__radd__(int_num))

bool_val = True
int_val = 223
print(int_val.__add__(bool_val))

print(bool(10))
print(bool)
print(dir(bool))
print(bool.__add__)
print(float.__radd__)

my_list = []
my_dict = {}
print(help(my_list.__eq__))
print(help(dict.__contains__))

