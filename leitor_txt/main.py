# O programa que usa a class Leitor do arquivo classes

from time import sleep
from classes import Leitor



while True:
    print('=' * 40 + '\n')
    try:
        arquivo = str(input('Nome do arquivo por favor: '))
        ar = arquivo
        if '.txt' not in arquivo:
            arquivo = arquivo + '.txt'
        arq = Leitor(arquivo)
        arq.mostrar()
    except:
        print()
        print('Erro, não foi possível abrir o arquivo!')
        sleep(2)
        print(f'Tente novamente, repare se o nome é esse mesmo: {ar}.')
        sleep(2)

    while True:
        continuar = str(input('Deseja ler outro arquivo? [sim/não] ')).lower()
        if continuar in 'simnãonao' and 's'in continuar or 'n' in continuar:
            break

    if continuar in 'nãonao' and 'n' in continuar:
        print('Saindo....')
        sleep(1)
        break
    

    
    
