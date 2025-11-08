from sympy import symbols, limit, oo
import sympy as sp
import time

#Este programa permite a un usuario calcular el teorema del valor medio usando el metodo de biseccion. 
#Materia: calculo numerico I
#Realizado por: Jeisi Rosales 

def main():
    # Presentacion del programa
    print("Bienvenido! Este programa permite calcular el teorema del valor medio usando el metodo de biseccion.")

    #ENTRADA DE DATOS
    x = symbols('x')

    # Funcion a resolver
    time.sleep(1)
    f_str = input("Ingrese la función trigonométrica (usa 'x' como variable, ej: sin(x) + 2*cos(x)): ")
    f = sp.sympify(f_str)

    # Valor del intervalo [a,b]
    print("Indique el intervalo para evaluar: ")
    a = float(input("Valor (a): "))
    b = float(input("Valor (b): "))

    # Valor del error relativo
    e_relativo = float(input("Indique el valor del error relativo: "))

    # VERIFICACION DE LA FUNCION
    # 1. verificar que sea continua
        #Calcular limite de la funcion
    limite_en_a = limit(f, x, a)
    valor_en_a = f.subs(x, a)

    if limite_en_a != valor_en_a: #Comprobar si el límite es igual al valor de la función
        print(f"\nLa funcion no es continua, no se puede usar el metodo de biseccion.")
    else:
        # 2. comprobar que f(a).f(b) < 0
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        if fa * fb >= 0:
            print(f"\nLa función no cambia de signo en el intervalo dado, por lo que no se puede aplicar el método de bisección.")
        else:
            i = 1
            print("\nInteracciones: ")
            metodo_biseccion(f, x, e_relativo, a, b, i)

# METODO DE BISECCION
def metodo_biseccion(f, x, e_relativo, a, b, i):
            fa = f.subs(x, a)
            # Calcular el punto medio c = (a + b) / 2
            c = (a + b) / 2
            print(f"Interaccion {i}: {c}")
            # Evaluar f(c)
            fc = f.subs(x, c)
            # Calcular error relativo e_relativo = (c - a) / c
            e = (c - a) / c
            print(f"Error relativo = {e}")
            # Determinar en que subintervalo [a, c] o [c, b] hay un cambio de signo
            if e < e_relativo:
                return print(f"\nResultado:\np = Interaccion {i} = {c}\nError relativo:{e}")
            else:
                if fa > 0 and fc > 0:
                    return metodo_biseccion(f, x, e_relativo, c, b, i + 1)
                else: 
                    return metodo_biseccion(f, x, e_relativo, a, c, i + 1)

if __name__ == "__main__":

    main()
