from random import sample
print('=' * 150)
print(f'{"BINGO ELETRÔNICO":^150}')
print('=' * 150)
sorteados = list()
while True:
    sorteado = sample(range(1, 60), 1)
    if sorteado not in sorteados:
        sorteados.append(sorteado)
    print(f'O número sorteado foi: \033[1;32m{sorteado}\033[m')
    print('-' * 150)
    sorteados.sort()
    print(f'Os números que já foram sorteados:'
          f'\n{sorteados}')
    print('-' * 150)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Próximo número? [S|N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('=' * 150)
print('ACABOU')
