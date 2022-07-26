import random
import Sorteia
def sorteia_questao_inedida(dic,nivel,lista):
    continuar = True
    questoes = dic[nivel]
    sorteada = Sorteia.sorteia_questao(dic,nivel)
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
    