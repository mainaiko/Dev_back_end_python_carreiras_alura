produtos = {"morangos": 5.0, "bananas": 3.0, "laranjas": 2.5}
carrinho = {}

print("Produtos disponíveis: morangos, bananas, laranjas")

while True:
    item = input("\nDigite o item que deseja comprar (ou 'sair' para finalizar): ").lower()
    
    if item == 'sair':
        break
        
    if item in produtos:
        quantidade = int(input(f"Digite a quantidade de {item}(s) que deseja: "))
        carrinho[item] = carrinho.get(item, 0) + quantidade
    else:
        print("Item não disponível.")

print("\n--- Resumo da Compra ---")
valor_total_compra = 0.0

for item, quantidade in carrinho.items():
    valor_subtotal = quantidade * produtos[item]
    valor_total_compra += valor_subtotal
    print(f"Item: {item} | Quantidade: {quantidade} | Valor unitário: R$ {produtos[item]:.2f} | Subtotal do item: R$ {valor_subtotal:.2f}")

print(f"\nValor total da compra: R$ {valor_total_compra:.2f}")
