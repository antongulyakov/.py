#!/usr/bin/env python
# version python3


def input_num(num, limit):
    "check the input arguments"
    try:
        arg = float(input("введите {0}-е число (попытка 1 из {1}):".format(num, limit)))
    except (TypeError, ValueError):
        print("было введено не число!")
        attempt = 2
        while attempt <= limit:
            try:
                arg = float(input("введите {0}-е число (попытка {1} из {2}):".format(num, attempt, limit)))
            except (TypeError, ValueError):
                if attempt < limit:
                    print("было введено не число!")
                else:
                    print("вы не исправимы! в таком случае обнулим {}-е число".format(num))
                    arg = 0

                attempt += 1
    return arg


def input_digit(num, limit):
    attempt =  1
    while attempt <= limit:
        try:
            arg = int(input("введите {0}-е число (попытка {1} из {2}):".format(num, attempt, limit)))
            attempt += limit
        except (TypeError, ValueError):
            if attempt < limit:
                print("было введено не число!")
            else:
                print("вы не исправимы! в таком случае обнулим {}-е число".format(num))
                arg = 0
        attempt += 1
    return arg       
