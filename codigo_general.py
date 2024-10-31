def metodo_newton_raphson(funcion, derivada, inicial, tolerancia=1e-10, max_iteraciones=1000):
    aproximacion = inicial
    for _ in range(max_iteraciones):
        valor_funcion = funcion(aproximacion)
        valor_derivada = derivada(aproximacion)
        
        if valor_derivada == 0:
            print("La derivada es cero; el método falla.")
            return None
        
        nueva_aproximacion = aproximacion - valor_funcion / valor_derivada
        
        if abs(nueva_aproximacion - aproximacion) < tolerancia:
            return nueva_aproximacion
        
        aproximacion = nueva_aproximacion
    
    print("No se alcanzó la convergencia en el número máximo de iteraciones.")
    return None

print("Ingrese la función f(x) y su derivada  .")
codigo_funcion = input("Función f(x): ")
codigo_derivada = input("Derivada f'(x): ")

funcion = lambda x: eval(codigo_funcion)
derivada = lambda x: eval(codigo_derivada)

inicial = float(input("Ingrese la aproximación inicial: "))
tolerancia = float(input("Ingrese la tolerancia deseada: "))

raiz = metodo_newton_raphson(funcion, derivada, inicial, tolerancia)

if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")
