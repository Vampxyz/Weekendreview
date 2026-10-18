dinheiro = int(input("\nDigite o valor em reais: ")) # 160
notas = [50,20,10,5,1]
resto = [] # 10

print(f'\nPara sacar R$ {dinheiro} é preciso de: ')

for n in notas:
    notaAtual = dinheiro // n # 3
    restoAtual = dinheiro % n # 10
    
    resto.append(restoAtual)
    
    print(f'{notaAtual} notas de {n} - {notaAtual * n}')
    
# valor = int(input("Digite o valor em reais: "))
# notas = [50,20,10,5,1]

# for nota in notas:
#     quantidade = valor // nota
#     valor = valor % nota

#     if quantidade > 0:
#         print(f"{quantidade} notas de R$ {nota:.2f}")
