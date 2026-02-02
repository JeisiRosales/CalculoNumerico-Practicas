import math
from scipy.integrate import quad

def riemann_method(f, a, b, n):
    # Calcular el ancho de cada rectángulo 
    h = (b - a) / n
    
    # Calcular el valor Aproximado (Suma de Riemann)
    valor_aproximado = 0
    for i in range(n):
        x = a + i * h
        valor_aproximado += f(x) * h
        
    # Calcular el valor Real (Integral exacta)
    valor_real, _ = quad(f, a, b)
    
    # Calcular el Error Relativo
    if valor_real != 0:
        error_relativo = abs((valor_real - valor_aproximado) / valor_real)
    else:
        # Manejo de caso borde si la integral real es 0
        error_relativo = abs(valor_real - valor_aproximado) 

    # --- Salida de resultados ---
    print("-" * 40)
    print(f"Resultados para n = {n} iteraciones:")
    print("-" * 40)
    print(f"Valor Real:        {valor_real:.6f}")
    print(f"Valor Aproximado:  {valor_aproximado:.6f}")
    print(f"Error Relativo:    {error_relativo:.6%}") # Formato porcentaje
    print("-" * 40)
    
    return valor_aproximado, error_relativo

# --- Bloque de Ejecución (Ejemplo) ---
if __name__ == "__main__":
    print("--- Calculadora de Integración por Riemann ---")
    
    # Entrada de la función
    print("Ingresa la función en términos de x (ejemplo: x**2 o math.exp(x))")
    func_input = input("f(x) = ")
    
    # Convertir el texto del usuario en una función lambda real
    f = lambda x: eval(func_input, {"x": x, "math": math})
    
    # Entrada de límites e iteraciones
    try:
        a = float(input("Límite inferior (a): "))
        b = float(input("Límite superior (b): "))
        n = int(input("Número de iteraciones (n): "))
        
        # Ejecutar el método
        riemann_method(f, a, b, n)
        
    except ValueError:
        print("Error: Por favor ingresa números válidos para a, b y n.")
    except Exception as e:
        print(f"Ocurrió un error con la función: {e}")