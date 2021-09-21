def notas(*resp, sit=False):
    """
    A funcao notas e responsavel por informar a maior, menor, media e a situacao
    de um aluno.
    :param resp = atribui os diversos valores escolhidos pelo usuário
    :boletim['Maior'] = informa a maior nota do aluno.
    :boletim['Menor'] = informa a menor nota do aluno.
    :boletim['Media'] = informa a media aritimetica do aluno.
    :notas(sit=False) = (Opcional) - caso este parametro esteja indicado como True, sera mostrada
    se a situacao do aluno esta BOA (media>=6) ou RUIM (media<6)

    """
    boletim = {}
    boletim['Total'] = len(resp)
    boletim['Maior'] = max(resp)
    boletim['Menor'] = min(resp)
    boletim['Média'] = sum(resp)/len(resp) 
    if sit==True:
        if boletim['Média'] >= 6:
            boletim['Situação'] = 'BOA'
            return boletim
        else:
            boletim['Situação'] = 'RUIM'
            return boletim
    return f'{boletim}'


resp = notas(5.5, 7, 7, 7.8)
print(resp)
help(notas)