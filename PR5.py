def calculator(num1,num2,tipe):
    choice = input('addition / substraction / multiplication / divide')
    tipe = input('in integer or float')

    if choice == 'addition' or choice == '+':
        ans = int(num1) + int(num2)
    elif choice == 'substraction' or choice == '-':
        ans = int(num1) - int(num2)
    elif choice == 'multiplication' or choice == '*':
        ans = int(num1) * int(num2)
    else:
        ans = int(num1) / int(num2)

    if tipe == 'int' or 'integer':
        print(ans)
    elif tipe == 'float':
        print(float(ans))
    else:
        return None
print(calculator(input(),input(),input()))
