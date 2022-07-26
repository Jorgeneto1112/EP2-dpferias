import random
from termcolor import colored, cprint
from exercicios import Transforma_Base_de_Questões
from exercicios import Sorteia_uma_Questão_Inédita
from exercicios import Valida_Uma_Questão
from exercicios import Questão_para_Texto
from exercicios import Gera_Ajuda_em_uma_Questão
# valida todas as questoes
# eu utilizei apenas o valida questao, nisso pegando apenas as questoes validadas 
lista_dados_nova = []
dados = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]
for questao in dados:
    validada = Valida_Uma_Questão.valida_questao(questao)
    if validada == {}:
        lista_dados_nova.append(questao)

# transforma base de questoes
dados_novo = Transforma_Base_de_Questões.transforma_base(lista_dados_nova)

# variaveis
rodar_questao = True
lista_ja_sorteadas = []
dinheiro = 0
pulos = 3
ajuda = 2
n = 1
lista_ajuda = []
lista_dificuldade = ['facil','facil','facil','medio','medio','medio', 'dificil','dificil','dificil']
i = 0
lista_premio = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
lista_quant_respostas = []
lista_alternativas = ['A','B','C','D','ajuda','pula','parar']
continuar = True
# inicia o jogo

cprint('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!','yellow')

pergunta_nome = input('qual sei nome? ')

print(f'Ok {pergunta_nome}, você tem direito a pular 3 vezes e 2 ajudas!')
cprint('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ','cyan')
tecla_para_continuar = input('Aperte ENTER para continuar...')
print('O jogo já vai começar! Lá vem a primeira questão! ')
print('Vamos começar com questões do nível {0}!'.format(lista_dificuldade[i]))
tecla_para_continuar = input('Aperte ENTER para continuar...')

# inicio do loop que fica perguntando a resposta
while rodar_questao == True:
    # utilizei apenas o sorteia uma questao inedita, pois eu ja utilzo o valida questao no valida questao inedita
    ja_foi_sorteada = Sorteia_uma_Questão_Inédita.sorteia_questao_inedida(dados_novo,lista_dificuldade[i],lista_ja_sorteadas)
    lista_ja_sorteadas.append(ja_foi_sorteada)
    mostrar_questao = Questão_para_Texto.questao_para_texto(ja_foi_sorteada,n)
    correta = ja_foi_sorteada['correta']
    print(mostrar_questao)
    resposta = input('Qual sua resposta?!')
    if resposta not in lista_alternativas:
        cprint('Opção inválida!','red')
        cprint('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!','cyan')
        while continuar == True:
            resposta = input('Qual sua resposta?!')
            if resposta in lista_alternativas:
                continuar = False
            else:
                cprint('Opção inválida!','red')
                cprint('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!','cyan')
    elif resposta == 'ajuda':
        dica = Gera_Ajuda_em_uma_Questão.gera_ajuda(ja_foi_sorteada)
        if ajuda == 0:
            cprint('Não deu! Você não tem mais direito a ajuda!')
        elif len(lista_ajuda) == 0:
            lista_ajuda.append(1)
            ajuda -= 1
            print('Ok, lá vem ajuda! Você ainda tem {0} ajudas!'.format(ajuda))
            cprint(dica,'green')
        elif len(lista_ajuda) != 0:
            lista_ajuda.append(1)
            print('Não deu! Você já pediu ajuda nesta questão!')
    elif resposta == 'pula':
        pulos -= 1
        if pulos == 0:
            print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
            ja_foi_sorteada = Sorteia_uma_Questão_Inédita.sorteia_questao_inedida(dados_novo,lista_dificuldade[i],lista_ja_sorteadas)
            lista_ja_sorteadas.append(ja_foi_sorteada)
            mostrar_questao = Questão_para_Texto.questao_para_texto(ja_foi_sorteada,n)
            print(mostrar_questao)
        elif pulos > 0:
            print('Ok, pulando! Você ainda tem {0} pulos!'.format(pulos))
            ja_foi_sorteada = Sorteia_uma_Questão_Inédita.sorteia_questao_inedida(dados_novo,lista_dificuldade[i],lista_ja_sorteadas)
            lista_ja_sorteadas.append(ja_foi_sorteada)
            mostrar_questao = Questão_para_Texto.questao_para_texto(ja_foi_sorteada,n)
            print(mostrar_questao)
        elif pulos <= 0:
            cprint('Não deu! Você não tem mais direito a pulos!','red')
    elif resposta == 'parar':
        sim_nao = input('Deseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {0}!'.format(dinheiro))
        if sim_nao == 's':
            print('Ok! Você parou e seu prêmio é de R$ {0}'.format(dinheiro))
            rodar_questao = False
            break
    elif resposta == correta:
        if len(lista_quant_respostas) == 3:
            dinheiro = lista_premio[i]
            i += 1
            n += 1
            print('Você passou para o nível MEDIO!')
        if len(lista_quant_respostas) == 6:
            dinheiro = lista_premio[i]
            i += 1
            n += 1
            print('Você passou para o nível DIFICIL!')
        else:
            dinheiro = lista_premio[i]
            i += 1
            n += 1
            cprint(f'Você acertou! Seu prêmio atual é de R$ {dinheiro}','green')
    else:
        cprint('Que pena! Você errou e vai sair sem nada :(')
        break
        