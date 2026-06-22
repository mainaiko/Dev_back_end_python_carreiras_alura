def pedra_papel_tesoura(usuario_1, usuario_2):
    if usuario_1 == usuario_2:
        return "Empate"
    elif (usuario_1 == "pedra" and usuario_2 == "tesoura") or (usuario_1 == "tesoura" and usuario_2 == "papel") or (usuario_1 == "papel" and usuario_2 == "pedra"):
        return "Usuário 1 venceu"
    else:
        return "Usuário 2 venceu"
    

