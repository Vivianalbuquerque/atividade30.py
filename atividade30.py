# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
mediaidade = 0
somaidade = 0
nomemisvelho = ''
maioridadehomem = 0
mulhermenor20 = 0
for i in range(1,5):
    nome = str(input("qual seu nome?"))
    idade = int(input("digite sua idade:"))
    sexo = str(input("qual seu genero?"))
    somaidade +=idade
if sexo == "masculino" and idade >= maioridadehomem:
    maioridadehomem = idade
    nomemisvelho = sexo
if sexo == "feminino" and idade >20:
    mulhermenor20 += -1
else:
    print("sexo invalido")
mediaidade = somaidade/4
print(f"A média de idade do grupo{mediaidade} anos.")
print(f"Ao todo são {mulhermenor20} mulheres com menos de 20 anos.")
print(f"o homem mais velho tem {maioridadehomem} anos e se chama {nomemisvelho}")