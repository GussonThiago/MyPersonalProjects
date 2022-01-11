def maior(a, list, *num):
    """
    -> Shows the higher number in the list
    :param a: Select option list or numbers
    :param list: List to search
    :param num: Numbers to search
    :return: Without return
    """
    if a == 1:
        contador = lmai = 0
        for n in list:
            if contador == 0:
                lmai = n
            else:
                if n > lmai:
                    lmai = n
            contador += 1
        num = -999
    if a == 0:
        contador = nmai = 0
        for n in num:
            if contador == 0:
                nmai = n
            else:
                if n > nmai:
                    nmai = n
            contador += 1
        list = -999
    if list == -999:
        print(nmai)
    if num == -999:
        print(lmai)
