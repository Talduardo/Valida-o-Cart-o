'''
Visa | Começa sempre com o número 4.
MasterCard | Começa com dígitos entre 51 e 55, ou entre 2221 a 2720.
Elo | Pode começar com vários intervalos, como 4011, 4312, 4389, entre outros.
American Express | Inicia com 34 ou 37.
Discover | Começa com 6011, 65, ou com a faixa de 644 a 649.
Hipercard | Geralmente começa com 6062.
'''

def bandeira_cartao(credit_card_number):
    if credit_card_number.startswith('4'):
        return 'Visa'
    elif credit_card_number[:2] in ['51', '52', '53', '54', '55'] or 2221 <= int(credit_card_number[:4]) <= 2720:
        return 'MasterCard'
    elif credit_card_number[:4] in ['4011', '4312', '4389'] or credit_card_number[:3] in ['431', '438']:
        return 'Elo'
    elif credit_card_number[:2] in ['34', '37']:
        return 'American Express'
    elif credit_card_number.startswith('6011') or credit_card_number[:2] == '65' or 644 <= int(credit_card_number[:3]) <= 649:
        return 'Discover'
    elif credit_card_number.startswith('6062'):
        return 'Hipercard'
    else:
        return 'Bandeira não reconhecida'