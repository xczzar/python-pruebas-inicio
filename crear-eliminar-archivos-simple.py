import os

def crear_archivos(nombre,num, extension):
    for i in range(1, num+1):
        with open(f"{nombre}{i}.{extension}","w") as f:
            pass

#AQUÍ INTRODUZCA EL NOMBRE, NÚMERO DE ARCHIVOS  Y EXTENSIÓN

crear_archivos("ejercicio",6,"py")

def eliminar_archivos(nombre, num, extension):
        for i in range(1,num+1):
            try:
                os.remove(f"{nombre}{i}.{extension}")
            
            except FileNotFoundError:
                 print(f"Archivo: '{nombre}{i}.{extension}' no localizado.")
             
             
#AQUI INTRODUZCA EL NOMBRE, NUMERO DE ARCHIVOS Y EXTENSIÓN            

eliminar_archivos("ejercicio", 6, "py")