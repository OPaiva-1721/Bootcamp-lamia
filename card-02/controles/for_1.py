#for i in range(10):
#   print(i)

#For i in range(1,11):
#   print(i)

# for i in range(1,100,7):
#   print(i)

#for i in range(20, 0, -3):
#    print(i)

#nums = [1, 2, 3, 4, 5]
#for n in nums:
#    print(n, end=" ")

#texto = "Python é uma linguagem de programação incrível!"
#for letra in texto:
#    print(letra, end=" ")

#for n in {1, 2, 3, 4, 4, 4}:
#    print(n, end=" ")

produto = {
    "nome": "Caneta",
    "preco": 1.50
}

#for atrib in produto:
#    print(atrib, produto[atrib])

for atrib, valor in produto.items():
    print(atrib, valor, end=" ")

print('')    

for atrib, valor in produto.items():
    print(valor, end=" ")

print('')

for valor in produto.values():
    print(valor, end=" ")

print

for atrib in produto.keys():    
    print(atrib, end=" ")