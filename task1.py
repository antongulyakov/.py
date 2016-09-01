#!/usr/bin/env python
# version python3


def arithmetic(i, j, op):
    "Returns the result of the operation of the two numbers"
    if op == "+":
        f = i+j
    elif op == "-":
        f = i-j
    elif op == "*":
        f = i*j
    elif op == "/":
        try:
            f = i/j
        except (ZeroDivisionError):
            f = 0
    else:
        f = None
    return f


def input_num(num, limit):
    "check the input arguments"
    try:
        arg = int(input("введите {0}-е число (попытка 1 из {1}):".format(num, limit)))
    except (TypeError, ValueError):
        print("было введено не число!")
        attempt = 2
        while attempt <= limit:
            try:
                arg = int(input("введите {0}-е число (попытка {1} из {2}):".format(num, attempt, limit)))
            except (TypeError, ValueError):
                if attempt < limit:
                    print("было введено не число!")
                else:
                    print("вы не исправимы! в таком случае обнулим {}-е число".format(num))
                    arg = 0

                attempt += 1
    return arg

arg1 = input_num(1, 3)
arg2 = input_num(2, 3)
op = input("введите одну из следующих математических операций (+,-,*,/):")

result = arithmetic(arg1, arg2, op)

if result is not None:
    print('резултат:')	
    print('{arg1}{op}{arg2}={res}'.format(arg1=arg1, arg2=arg2, op=op, res=result))
else:
    print(op, "- это неизвестная операция")
