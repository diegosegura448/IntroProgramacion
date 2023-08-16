#Python
#Ejercicio 1: 
'''
print('Hola Mundo.')

#Ejercicio 2:
Mensaje= 'Hola Mundo'
print(Mensaje)

#Ejercicio 3:
nombre=input("Escribe tu nombre: ")
print("Hola "+nombre+"!")
 
#Ejercicio 4:
print(((3+2)/(2*5))**2)

#Ejercicio 5:
horas=float(input("escriba la cantidad de horas: "))
costo=float(input("escriba valor por hora: "))
pago= horas*costo
print("Tu pago es: ",pago)
#Ejercicio 6
n= int(input("ENtero positivi: "))
suma= n*(n+1)/2
print("La suma del entero es: ",suma) 
#ejercicio 7:
peso=input("Digita tu peso en Kg: ")
estatura= input("Digita tu estatura en M:")
imc=round(float(peso)/float(estatura)**2,2)
print("Tú indice de masa corporal es: ",imc)'''
#----------------------Calse 5-------------------------#
'''n = 0
n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
if suma > 20:
  print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma)+ ", es un gran número!")
else:
  print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))

n = 0
m = 0
c = 0.0
r = 0
n = int(input("Introduce el dividendo (entero): "))
m = int(input("Introduce el divisor (entero): "))
c = n//m
r = n%m

print(str(n) + " entre " +  str(m) + " da un cociente " + str(c) + " y un resto " + str(r))'''

def Menu():
    """Funcion que Muestra el Menu"""
    print ("""************
    Calculadora
    ************
    Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    """)
def suma(a,b):
  return a+b

def resta(a,b):
  return a-b

def multiplicacion(a,b):
  return a*b

def division(a,b):
  if b==0:
    print("Error, Division entre 0")
  else:
    return a/b


def Calculadora():    
    Menu()
    opcion = int(input("Selecione Opcion\n"))
    
    x = float(input("Ingrese Numero\n"))
    y = float(input("Ingrese Otro Numero\n"))
    if (opcion==1):
        print ("La Suma es:", suma(x,y))
    elif(opcion==2):
        print ("La Resta es:", resta(x,y))
        
    elif(opcion==3):
        print ("La Multiplicacion es:", multiplicacion(x,y))
        
    elif(opcion==4):
        print ("La Division es:", division(x,y))


Calculadora()