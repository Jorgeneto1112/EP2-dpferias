def valida_questao(questao):
    novo_dic = {}
    lista_keys_principal = ['titulo','nivel','opcoes','correta']
    lista_keys = []
    for chaves in questao:
        lista_keys.append(chaves)
    for chaves in lista_keys_principal:
        if chaves not in lista_keys:
            novo_dic[chaves] = 'nao_encontrado'
    if len(lista_keys) != 4:
        novo_dic['outro'] = 'numero_chaves_invalido'
    for chaves, values in questao.items():
        if values != str:
            novo_dic[chaves] = 'vazio'
            
    return novo_dic
    
        
print(valida_questao({
  'titulo': '',
  'nivel': 'moleza',
  'opcoes': {'A': '  ', 'B': '85', 'C': '89', 'D': '\t'}
}))