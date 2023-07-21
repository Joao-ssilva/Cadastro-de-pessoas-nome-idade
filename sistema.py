from  lib.interface import *
from time import sleep
from lib.arquivo import *


arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
    

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o contéudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Opção 3')
        cabecalho('Saindo so sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opçao válida! \033[m')
        sleep(2)

