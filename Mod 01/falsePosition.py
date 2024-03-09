def falsa_posicao(funcao, a, b, tolerancia=1e-6, max_iter=100):
    """
    Método da Falsa Posição para encontrar a raiz de uma função no intervalo [a, b].

    :param funcao: Função para a qual queremos encontrar a raiz.
    :param a: Extremidade esquerda do intervalo.
    :param b: Extremidade direita do intervalo.
    :param tolerancia: Tolerância para a solução.
    :param max_iter: Número máximo de iterações.
    :return: Aproximação da raiz da função.
    """

    if funcao(a) * funcao(b) > 0:
        raise ValueError("A função deve ter sinais opostos em a e b para garantir a existência de uma raiz.")

    for i in range(max_iter):
        # Calcular o ponto intermediário
        c = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))

        # Verificar a tolerância
        if abs(funcao(c)) < tolerancia:
            return c

        # Atualizar os limites
        if funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c

    raise ValueError("O método da falsa posição atingiu o número máximo de iterações sem convergir.")

# Exemplo de uso:
def funcao_exemplo(x):
    return x**3 - 6*x**2 + 11*x - 6

a = 1
b = 4
raiz_aproximada = falsa_posicao(funcao_exemplo, a, b)

print(f"A raiz aproximada é: {raiz_aproximada}")
