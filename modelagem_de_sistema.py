class OmniShopPedido:
    def __init__(self, valor_produtos: float, valor_frete: float, forma_pagamento: str):
        self.valor_produtos = valor_produtos
        self.valor_frete = valor_frete
        self.forma_pagamento = forma_pagamento.upper()
        self.status = "Reservado"

    def calcular_total(self) -> float:
        """Aplica a Regra de Negócio de desconto do PIX nos produtos (RNF/RN relacionado)."""
        subtotal = self.valor_produtos
        if self.forma_pagamento == "PIX":
            subtotal = self.valor_produtos * 0.90
        
        return subtotal + self.valor_frete

    def cancelar_por_falta_retirada(self) -> float:
        """Aplica as Regras de Negócio de cancelamento após 7 dias (RN01 e RN02)."""
        self.status = "Cancelado por Expiração"

        valor_pago_produtos = self.valor_produtos
        if self.forma_pagamento == "PIX":
            valor_pago_produtos *= 0.90

        taxa_administrativa = valor_pago_produtos * 0.05
        credito_loja = valor_pago_produtos - taxa_administrativa
        
        return credito_loja

if __name__ == "__main__":

    pedido = OmniShopPedido(valor_produtos=200.0, valor_frete=20.0, forma_pagamento="PIX")
    
    total_com_desconto = pedido.calcular_total()
    print(f"Total a pagar (com 10% de desconto no PIX): R$ {total_com_desconto:.2f}")

    credito = pedido.cancelar_por_falta_retirada()
    print(f"Status do pedido: {pedido.status}")
    print(f"Crédito gerado na loja (após retenção de 5%): R$ {credito:.2f}")