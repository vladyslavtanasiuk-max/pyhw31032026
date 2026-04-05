while True:
    a = int(input("введіть 1 число: "))
    op = str(input("введіть знак обчислення: (+,-,*,/) "))
    b = int(input("введіть 2 число: "))

    if op == "/" and b == 0:
        print('Ділленя на 0 неможливе')
    else:
        t = f"{a}{op}{b}"
        print(f"{t} = {str(eval(t))}")