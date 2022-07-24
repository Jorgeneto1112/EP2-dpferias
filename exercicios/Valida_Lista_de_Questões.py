import Valida_Uma_Questão
def valida_questoes(lista):
    lista_final = []
    for questao in lista:
        erros = Valida_Uma_Questão.valida_questao(questao)
        lista_final.append(erros)
    return lista_final
print(valida_questoes([{'titulo': 'Qual a capital do Brasil?', 'nivel': 'facil', 'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'}, 'correta': 'A'}, {'titulo': 'Qual destes parques não se localiza em São Paulo?!', 'nivel': 'facil', 'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'}, 'correta': 'D'}, {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?', 'nivel': 'medio', 'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'}, 'correta': 'C'}]
))