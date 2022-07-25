import random
from termcolor import colored, cprint
from exercicios import Valida_Uma_Questão
from exercicios import Valida_Lista_de_Questões
from exercicios import Transforma_Base_de_Questões
from exercicios import Sorteia_Uma_Questão
from exercicios import Sorteia_uma_Questão_Inédita
from exercicios import Questão_para_Texto
from exercicios import Gera_Ajuda_em_uma_Questão
# inicia o jogo
continuar = True 
while continuar == True:
    cprint('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!','yellow')

    pergunta_nome = input('qual sei nome? ')

    print(f'Ok {pergunta_nome}, você tem direito a pular 3 vezes e 2 ajudas!')
    cprint('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ','cyan')
    tecla_para_continuar = input('Aperte ENTER para continuar...')
    print('O jogo já vai começar! Lá vem a primeira questão! ')
    print('Vamos começar com questões do nível FACIL!')
    tecla_para_continuar = input('Aperte ENTER para continuar...')
    continuar = False
