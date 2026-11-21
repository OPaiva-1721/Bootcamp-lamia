total = 0
nota = 0
qtd = 0

while nota != -1:
    nota = float(input("Digite um número ou -1 para sair: "))
    if nota != -1:
        total += nota
        qtd += 1
        
print(f"A média das notas é: {total/qtd}")