def exibir_saudacao(nome):
    """
    Exibe uma saudação personalizada.

    """
    print(f"Olá, {nome}! Seja bem-vindo(a) ao mundo do Python e git!")

    if __name__ == "__main__":
        nome_usuario = input("qual é o seu nome?,")
        exibir_saudacao(nome_usuario)