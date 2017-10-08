def factor(x):
    try:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        elif x!=0 and x!=1:
            return x*factor(x-1)
    except (TypeError):
        return None


print(factor(10))
