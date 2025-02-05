# Description: Validação de projetos
from bandeiras import bandeira_cartao

def is_number_odd(number):
    if type(number) != int:
        raise ValueError('O valor informado não é um número inteiro.')
    if number % 2 == 0:
        return False
    else:
        return True
    