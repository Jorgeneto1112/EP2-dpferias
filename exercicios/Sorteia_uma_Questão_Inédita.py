import random
def sorteia_questao_inedida(dic,nivel,lista):
    continuar = True
    questoes = dic[nivel]
    sorteada = random.choice(questoes)
    if sorteada in lista:
        while continuar == True:
            sorteada = random.choice(questoes)
            if sorteada not in lista:
                continuar = False
        lista.append(sorteada)
        return sorteada
    else: 
        lista.append(sorteada)
        return sorteada
    