import sympy as sp
from sympy import symbols
import time
#Este programa permite a un usuario calcular el teorema del valor medio usando el metodo de Newton-Raphson. 
#Materia: calculo numerico I
#Realizado por: Jeisi Rosales (C.I: 2968571)

def main():
    # Presentacion del programa
    print("Bienvenido! Este programa permite calcular el teorema del valor medio usando el metodo de Newton-Raphson.")
    x = symbols('x')
    i = 0
    # Funcion a resolver
    time.sleep(1)
    f_str = input("Ingrese la funcion trigonometrica (usa 'x' como variable, ej: sin(x) + 2*cos(x)): ")
    f = sp.sympify(f_str)

    # Valor del intervalo [a,b]
    print("Indique el intervalo para evaluar: ")
    a = float(input("Valor (a): "))
    b = float(input("Valor (b): "))

    # Valor del Valor inicial Xo
    xi = float(input("Valor inicial (Xi): "))

    # Valor del error relativo
    e_relativo = float(input("Indique el valor del error relativo: "))

    # Definir las interacciones maximas
    i_max = int(input("Interacciones maximas: "))

    # Llamar al metodo
    newton_raphson(f, x, e_relativo, xi, i_max)

# Metodo de Newton-Raphson
def newton_raphson(f, x, e_relativo, xi, i_max):
    # Derivadas de la funcion
    f1 = sp.diff(f, x)   # Primera derivada
    f2 = sp.diff(f1, x)   # Segunda derivada

    # Evaluacion de las derivadas en el punto inicial
    f0_v = float(f.subs(x, xi)) # valor de f en xi
    f1_v = float(f1.subs(x, xi)) # valor de f' en xi
    f2_v = float(f2.subs(x, xi)) # valor de f'' en xi
    t_convergencia = (f0_v * f2_v) / (f1_v ** 2)
    
    print("\nTeorema de convergencia:")
    print(f"f(x) = {f} = {round(f0_v, 2)}\nf'(x) = {f1} = {round(f1_v, 2)}\nf''(x) = {f2} = {round(f2_v, 2)}\nTeorema de convergencia = {round(t_convergencia,2 )}\n")
    if abs(t_convergencia) >= 1:
        time.sleep(2)
        print("ADVERTENCIA: El método de Newton-Raphson puede no converger.\n")

    # Iteraciones del metodo
    print("Evaluacion de la sucesion:")
    for k in range(0, i_max):
        # Validaciones
        f0_val = f.subs(x, xi) # valor de f en xi
        f1_val = float(f1.subs(x, xi)) # valor de f' en xi
        if abs(f0_val) == 0:
            return print(f"Raíz exacta encontrada: {round(xi)}")
        if f1_val == 0:
            print("Derivada nula en xi; no se puede continuar.")
            return None
        
        # Evaluacion de la sucesion
        xi_new = xi - f0_val / f1_val
        err_rel = abs((xi_new - xi) / xi_new) if xi_new != 0 else abs(xi_new - xi)
        print(f"i-{k}: xi = {round(xi, 2)} | xi+1 = {round(xi_new, 2)} | er = {round(err_rel, 2)}")

        if err_rel < e_relativo:
            print(f"Convergencia alcanzada en iteración {k}: {round(xi_new, 2)}")
            return xi_new
        
        xi = xi_new

    return print("Se han alcanzado las iteraciones máximas sin converger.")

if __name__ == "__main__":
    main()