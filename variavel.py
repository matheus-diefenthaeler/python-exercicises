x = 2
# print(x + x)

# O Andre tem 32 de idade e mora na cidade de Sao Paulo.

nome = "Lucas"
idade = 33
cidade = "Rio de Janeiro"

# print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora na cidade ' + cidade)
mensagem = f'O {nome} tem {str(idade)} anos de idade e mora na cidade {cidade}'
print(mensagem.replace("idade", "IDADE"))


# imprime("Matheus", 31, "Vila Velha")


def imprime():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite a cidade voce mora: ")
    print("O", nome, "tem", idade, "anos de idade e mora na cidade de", cidade)


# imprime()

def calculaIdade():
    anoNasciimento = input("Digite o ano nascimento: ")
    idade = 2022 - int(anoNasciimento)
    print(idade)


# calculaIdade()


