def newton_raphson(funcion, derivada, valor_inicial, tolerancia=1e-10, max_iteraciones=1000):
    valor = valor_inicial
    for iteracion in range(max_iteraciones):
        funcion_valor = funcion(valor)
        derivada_valor = derivada(valor)
        if abs(derivada_valor) < 1e-10:
            return None
        siguiente_valor = valor - funcion_valor / derivada_valor
        if abs(siguiente_valor - valor) < tolerancia:
            return siguiente_valor
        valor = siguiente_valor
    return None

radio_pequeno = 3.04042e-6

def funcion_L1(x):
    return x**5 - (2 + radio_pequeno) * x**4 + (1 + 2 * radio_pequeno) * x**3 - (1 - radio_pequeno) * x**2 + 2 * (1 - radio_pequeno) * x + radio_pequeno - 1

def derivada_funcion_L1(x):
    return 5 * x**4 - 4 * (2 + radio_pequeno) * x**3 + 3 * (1 + 2 * radio_pequeno) * x**2 - 2 * (1 - radio_pequeno) * x + 2 * (1 - radio_pequeno)

def funcion_L2(x):
    return funcion_L1(x) - 2 * radio_pequeno * x**2

def derivada_funcion_L2(x):
    return 5 * x**4 - 4 * (2 + radio_pequeno) * x**3 + 3 * (1 + 2 * radio_pequeno) * x**2 - 2 * (1 - radio_pequeno) * x + 2 * (1 - radio_pequeno) - 4 * radio_pequeno * x

aproximacion_L1 = 0.5
aproximacion_L2 = 1.5

L1 = newton_raphson(funcion_L1, derivada_funcion_L1, aproximacion_L1)
L2 = newton_raphson(funcion_L2, derivada_funcion_L2, aproximacion_L2)

print(f"Coordenada x del punto L1: {L1}")
print(f"Coordenada x del punto L2: {L2}")
