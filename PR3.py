def print_sum(a, b):
    try:
        return (a**2,b**2)
    except TypeError:
        return (None)
print(print_sum(25,64))
print(print_sum(str(25),str(64)))
print(print_sum(25,str(64)))

