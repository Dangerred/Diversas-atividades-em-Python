from datetime import date

def voto(ano):
    votobri = date.today().year - ano
    if votobri >= 18:
        return f'Com {votobri} anos a votação é obrigatória!'
    elif 16 <= votobri < 18 or votobri > 65:
        return f'Com {votobri} anos a votação é FACULTATIVA!'
    else:
        return f'Com {votobri} anos a votação NÃO é obrigatória!'

print(voto(1945))
