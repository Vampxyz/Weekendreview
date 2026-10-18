def calcular_divisao_conta(valor_total, numero_pessoas, percentual_gorjeta = 10):
    percentual_gorjeta = percentual_gorjeta / 100
  
    if numero_pessoas <= 0:
        return f'É impossível dividir a conta para {numero_pessoas} pessoas!'
    
    valor_gorjeta = valor_total * percentual_gorjeta
    
    conta = (valor_gorjeta + valor_total) / numero_pessoas
    
    print(f'O valor da conta dividido para {numero_pessoas} é: {round(conta, 2)}')
    
    return conta

valor_total = float(input('Digite o valor da conta: '))
numero_pessoas = int(input('Digite a quantidade de pessoas: '))
percentual_gorjeta = float(input('Digite o percentual da gorjeta: '))

if percentual_gorjeta > 0:
    print(f'''
        Quer pagar a gorjeta de {int(percentual_gorjeta)}%? 
        S - Sim 
        N - Não
        ''')

    pergunta_gorjeta = input(f'\nDigite a opção desejada: ').strip().upper()

else:
    pergunta_gorjeta = 'N'



if pergunta_gorjeta == 'N':
    calcular_divisao_conta(valor_total, numero_pessoas, 0)

elif pergunta_gorjeta == 'S':
    calcular_divisao_conta(valor_total, numero_pessoas, percentual_gorjeta)
    
else:
    print('Resposta não corresponde com o que foi perguntado!')
