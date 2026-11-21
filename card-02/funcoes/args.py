def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total


# **kwargs recebe parâmetros nomeados e guarda em um dicionário
def resultado_final(**kwargs):
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status}'


print(soma(1))
print(soma(1, 2, 3))
print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(resultado_final(nome='Pedro', nota=7.3))
