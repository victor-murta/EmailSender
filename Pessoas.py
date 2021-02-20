import os
from time import sleep
arquivo = 'PessoasEmail.txt'

def creating_file(name):
    try:
        arquivo = open(name, 'wt+')
        arquivo.close()
    except :
        print(f'ERRO ao criar o arquivo {name}')
    else:
        print(f'Arquivo {name} criado com SUCESSO!!!')
        print(f'A rota do arquivo é {os.path.abspath(name)}')
        
def file_search(name):
    try:
        file = open(name,'rt')
    except :
        print(f'Infelizmente não encontrei a pasta {name}')
    else:
        print(f'Arquivo {name} encontrado')
        print('Pessoas cadastradas: ')
        print(file.read())
        #integrar
    finally:
        file.close()

def writting(arquivo,name= 'Desconhecido'):
    try:
        #wt write text
        #rt read text
        #at: append text
        file = open(arquivo, 'at')    
    except :
        print('Ocorreu algum ERRO ao acrescentar a pessoa')
    else:
        file.write(name)
    finally:
        file.close()

def people(arquivo):
    try:
        a = open(arquivo,'rt')
        return a.read()
    except :
        print(f'Não encontrei o arquivo {arquivo}')
        r = str(input('Deseja criar o arquivo (s/n): ')).strip().lower()[0]
        if r == 's':
            creating_file(arquivo)
        else:
            pass
    else:
        print('Email mandado com SUCESSO para as pessoas')


