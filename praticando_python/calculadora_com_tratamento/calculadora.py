def calculadora(valor1, valor2, operacao):
    if operacao == "soma":
        return valor1 + valor2
    elif operacao == "subtracao":
        return valor1 - valor2
    elif operacao == "multiplicacao":
        return valor1 * valor2
    elif operacao == "divisao":
        if valor2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return valor1 / valor2
    else:
        raise ValueError("Operação inválida. Escolha entre soma, subtracao, multiplicacao ou divisao.")