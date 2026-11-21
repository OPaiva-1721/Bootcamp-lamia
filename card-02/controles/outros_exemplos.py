pessoas = ["Gui", "Rebeca"]
adjetivos = ["Sapeca", "inteligente"]

for pessoa in pessoas:
    for a in adjetivos:
        print(f"{pessoa} é {adjetivo}")

for i in [1, 2, 3, 4, 5]:
    pass

for i in range(1, 6):
    if i % 2 == 1:
        continue
    print(i)

for i in range(1, 6):
    if i == 5:
        break
    print(i)

print("Fim do programa")

