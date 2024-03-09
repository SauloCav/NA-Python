def bisseccao(funcao, a, b, tolerancia=1e-6, max_iter=100):

    if funcao(a) * funcao(b) > 0:
        raise ValueError("A função deve ter sinais opostos em a e b para garantir a existência de uma raiz.")

    for i in range(max_iter):
        # Calcular o ponto intermediário
        c = (a + b) / 2

        # Imprimir valores em cada iteração
        print(f"Iteração {i+1}: a = {a}, b = {b}, f(a) = {funcao(a)}, f(b) = {funcao(b)}, x = {c}, f(x) = {funcao(c)}")

        # Verificar a tolerância
        if abs(funcao(c)) < tolerancia:
            return c

        # Atualizar os limites
        if funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c

    raise ValueError("O método da bissecção atingiu o número máximo de iterações sem convergir.")

# Exemplo de uso:
def funcao_exemplo(x):
    return x**3 - 9*x + 5

a = 0.5
b = 1
raiz_aproximada = bisseccao(funcao_exemplo, a, b)

print(f"\nA raiz aproximada é: {raiz_aproximada}")
