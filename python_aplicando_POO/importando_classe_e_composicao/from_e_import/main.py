from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alterar_estado()

restaurante_praca.receber_avaliacao('natalia', 10) # atribuindo uma avaliação ao metodo avaliação


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()

