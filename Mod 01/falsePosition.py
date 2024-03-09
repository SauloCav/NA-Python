def falsa_posicao(funcao, a, b, tolerancia=1e-6, max_iter=100):
    if funcao(a) * funcao(b) > 0:
        raise ValueError("A função deve ter sinais opostos em a e b para garantir a existência de uma raiz.")

    for i in range(max_iter):
        c = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))

        print(f"Iteração {i+1}: a = {a}, b = {b}, f(a) = {funcao(a)}, f(b) = {funcao(b)}, x = {c}, f(x) = {funcao(c)}")

        if abs(funcao(c)) < tolerancia:
            return c

        if funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c

    raise ValueError("O método da falsa posição atingiu o número máximo de iterações sem convergir.")

def funcao_exemplo(x):
    return x**4 - 26*x**2 + 24*x + 21

a = 1
b = 2
raiz_aproximada = falsa_posicao(funcao_exemplo, a, b)

print(f"\nA raiz aproximada é: {raiz_aproximada}")
