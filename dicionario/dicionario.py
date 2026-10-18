# pergunte posição e quantidade. Valide a posição (0 a len − 1) e o estoque. Se der certo, baixe o estoque e mostre o total; senão, avise o motivo.
produtos = [
    {"nome": "Arroz", "preco": 25.90, "estoque": 10}, # 0
    {"nome": "Feijão", "preco": 8.50, "estoque": 20}, # 1
    {"nome": "Macarrão", "preco": 5.00, "estoque": 15} # 2
]

for i, p in enumerate(produtos, start=1):
    print(f'{i}: {p}')

pos = int(input('Digite a posição do produto que você deseja: ')) - 1 # 1
quantidade = int(input('Digite a quantidade: ')) # 10
estoqueProdutoSelecionado = produtos[pos]['estoque'] # 20

# Verificando se o produto existe na lista
if pos + 1 <= len(produtos):
    
    # Verificando se a quantidade digitada é possivel subtrair no estoque
    if quantidade <= estoqueProdutoSelecionado:
        produtos[pos]['estoque'] -= quantidade
        print(f'O {produtos[pos]['nome']} agora tem o estoque = {estoqueProdutoSelecionado}')

    else:
        print(f'{estoqueProdutoSelecionado}')

else:
    print('Produto não encontrado no banco de dados...')