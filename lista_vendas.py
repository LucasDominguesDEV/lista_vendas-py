""" Crie uma função analisar_vendas(vendas) que: Receba uma lista de vendas (valores numéricos)

Ignore valores inválidos

Retorne: total vendido, média das vendas e quantidade de vendas válidas

📌 Desafio extra (opcional)

Se a lista estiver vazia ou não tiver valores válidos, retorne uma mensagem de erro

 📌 Conceitos treinados
função, list, for, if, try_except, return """

produtos = [
    ["Geladeira",       1200.50, "A001"],
    ["Fogão",           850.00,  "B014"],
    ["Televisão",       2300.90, "C322"],
    ["Microondas",      150.75,  "D087"],
    ["Sofá",            4999.99, "E910"],
    ["Mesa de jantar",  0,       "F111"],   # valor inválido
    ["AirFryer",       -300,    "G404"],   # valor inválido
]

def analisar_vendas(vendas):
    total_vendido = 0
    quantidade_vendas = 0
    lista_vendidos = []

    for venda in vendas:
        if venda[1] <= 0:
            continue

        quantidade_vendas += 1
        total_vendido += venda[1]
        lista_vendidos.append(venda[0])

    if quantidade_vendas == 0:
        return [], 0, 0, 0

    media_vendas = total_vendido / quantidade_vendas

    return lista_vendidos, total_vendido, quantidade_vendas, media_vendas


vendidos, total, quantidade, media = analisar_vendas(produtos)

if not vendidos:
    print("Nenhuma venda válida encontrada.")
else:
    print("Lista de produtos vendidos:")
    for produto in vendidos:
        print(f"- {produto}")

    print(f"\nTotal vendido: R${total:.2f}")
    print(f"Quantidade de vendas: {quantidade}")
    print(f"Média das vendas: R${media:.2f}")
