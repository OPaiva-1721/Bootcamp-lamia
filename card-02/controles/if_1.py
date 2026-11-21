nota = float(input("Digite a nota do aluno: "))
comportado = True if input("O aluno se comportou bem? (s/n): ").lower() == 's' else False

if nota >= 9 and comportado:
    print("Aprovado com louvor!")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5.5:
    print("Recuperação!")
elif nota >= 3.5:
    print("Recuperação + Trabalho!")
else:
    print("Reprovado!")