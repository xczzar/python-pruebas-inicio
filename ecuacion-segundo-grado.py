from math import sqrt

def calculo_ecuacion():
    while True:
        try:
            a=int(input("\nEscribe el primer valor (x²): "))
            b=int(input("\nEscribe el segundo valor (x): "))
            c=int(input("\nEscribe el valor independiente: "))

            if a==0:
                print("\n***\nError: 'a' no puede ser 0, sino no sería una ecuacion de segundo grado.\n***")
                continue

            break
            
        except ValueError:
            print("Error: *** Introduce un numero entero ***")


    discriminante= pow(b,2) -4*a*c
    
    if discriminante <0:
        print(f"\nLa ecuación no tiene soluciones reales. Discriminante: {discriminante}")
    else:
        raiz= sqrt(discriminante)
        formula_resultado_positivo=(-b + raiz) / (2*a)
        formula_resultado_negativo=(-b - raiz) / (2*a)
    
        print(f"\nSolución 1 (+): {formula_resultado_positivo}")
        print(f"Solución 2 (-): {formula_resultado_negativo}")

calculo_ecuacion()