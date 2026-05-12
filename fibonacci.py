def fibonacci(num):
    a,b=0,1
    for i in range(num):
        print(a, end=" ")
        a,b=b,a+b
    print()

fibonacci(10)

print("hola Mundo")
print("skibidi")

def saludar(nombre):
    return f"Hola {nombre}!"

print(saludar("Pepito"))