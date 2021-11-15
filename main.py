from bib import *

op = True
while op:
    print(40*'==')
    print('Converter Imagens => txt')
    print(40*'--')
    print()
    diretorio = str(input('Diretorio onde estão as imagens: '))
    converter(diretorio)

    print()
    print(40*'==')
    print()
    opcao = input("Aperte 'f' para finalizar. ")
    if opcao.lower() == 'f':
        op = False

    print()
    print(40*'--')
    print('FIM!!!')
    print(40*'==')
    print()
