def saudacao(nome = "Pessoa", idade = 20):
    print(f"bom dia, {nome}! Você tem {idade} anos.")

#def saudacao():
#    print("Boa tarde!")

def soma_e_mult(a,b,x):
    return a + b * x

if __name__ == "__main__":
    saudacao()
    saudacao("João")
    saudacao("Alice", 25)
    saudacao(idade = 30)