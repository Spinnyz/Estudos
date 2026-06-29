produtos = [
    {'nome':'Produto A', 'preco':10},
    {'nome':'Produto B', 'preco':20},
    {'nome':'Produto C', 'preco':30},
]


novos_produtos = [
    {"nome":produto["nome"], 
    "preco":produto["preco"]*2}
    if produto["preco"] > 20 else {**produto}
    for produto in produtos 
        
]




print(novos_produtos)

