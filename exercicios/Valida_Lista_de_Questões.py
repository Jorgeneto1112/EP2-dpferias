import Valida_Uma_Questão
def valida_questoes(lista):
    lista_final = []
    for questao in lista:
        erros = Valida_Uma_Questão.valida_questao(questao)
        lista_final.append(erros)
    return lista_final
