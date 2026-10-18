# Criar uma função chamada calcular_divisao_conta que receba os dados da despesa e retorne o valor exato que cada pessoa deve pagar.

# A função deve receber três parâmetros:

    - valor_total (float): O valor total consumido na mesa.

    - numero_pessoas (int): A quantidade de pessoas que vão dividir a conta.

    - percentual_gorjeta (float, opcional): A porcentagem da gorjeta (deve ter o valor padrão de 10, representando 10%).

# A função deve verificar se o numero_pessoas é menor ou igual a zero. Se for, deve retornar uma mensagem de erro ou 0, evitando erro de divisão por zero.

# A função deve calcular o valor da gorjeta, somar ao valor total e dividir igualmente entre as pessoas.

# O resultado retornado deve ser arredondado para duas casas decimais (usando a função round()).