numeros = list()

for c in range(1, 6):
    numeros.append(int(input(f'{c}º numero a adicionar: ')))
print(numeros)


def menor(a, list, *num):
    """
    -> Shows the lowest number in the list
    :param a: Select option list or numbers
    :param list: List to search
    :param num: Numbers to search
    :return: Without return
    """
    if a == 1:
        contador = lmen = 0
        for n in list:
            if contador == 0:
                lmen = n
            else:
                if n < lmen:
                    lmen = n
            contador += 1
        num = -999
    if a == 0:
        contador = nmen = 0
        for n in num:
            if contador == 0:
                nmen = n
            else:
                if n < nmen:
                    nmen = n
            contador += 1
        list = -999
    if list == -999:
        print(nmen)
    if num == -999:
        print(lmen)


menor(1, numeros)
menor(0, 0, 5, 2, 3, 4, 5, 6)
