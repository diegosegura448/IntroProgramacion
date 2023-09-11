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
#*********************************************Calculadora****************************************
'''
def Menu():
    print ("""************
    Calculadora
    ************
    Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir
    """)
  
def suma(a,b):
  return a+b

def resta(a,b):
  return a-b

def multiplicacion(a,b):
  return a*b

def division(a,b):
  if b==0:
    print("Error, División entre 0")
  else:
    return a/b


def Calculadora():    
    Menu()
    opcion = int(input("Selecione Opción\n"))
    
    x = float(input("Ingrese Primer Número\n"))
    y = float(input("Ingrese Segundo Número\n"))
  
    if (opcion==1):
        print ("La Suma es:", suma(x,y))
    elif(opcion==2):
        print ("La Resta es:", resta(x,y))
        
    elif(opcion==3):
        print ("La Multiplicación es:", multiplicacion(x,y))
        
    elif(opcion==4):
        print ("La División es:", division(x,y))


Calculadora()
#*******************************************************************************************************
#****************************************ctaAhorro**********************************************

def intereses(inv):
  d= inv
  if (d >0 and d<1000000):
    return 2
  elif(d>=1000000 and d < 2000000):
    return 5
  else: 
    return 7

def calBalance(int, inv):
  n= int
  d = inv
  return round((d*(1+(n/100))),2)
  
def ctaAhorro():
  #inversion,interes,b1,b2,b3 = 0.0
  inversion = float(input("Ingrese el valor de la inversión: "))
  interes=intereses(inversion)
  b1=calBalance(interes,inversion)
  b2= calBalance(interes,b1)
  b3= calBalance(interes,b2)
  print("Balance año 1: " + str(b1) + " Balance año 2: " + str(b2) + " Balance año 3: " + str(b3))

ctaAhorro()'''
#******************************************************************************
#*****************************areasFig****************************************
'''def areaTriangulo(b,a):
  return(b*a)/2

def areaCuadrado(bc,ac):
  return bc*ac

def areaCirculo(r):
  return(3.14169*(r**2))

def areaFig():
  area=0.0
  figura=""
  figura = input("Escriba la figura a la que se le desea calcular el area: ")
  
  if (figura.lower()=="triangulo"):
    base=0.0
    altura=0.0
    base = float(input("ingrese la base:"))
    altura= float(input("Ingrese la altura: "))
    area = areaTriangulo(base,altura)
    print("El area del triangulo es: ", area)

areaFig()

'''

#******************Taller****************************
#1
'''
2012 es bisiesto
2010 no es bisiesto
2000 es bisiesto
1900 no es bisiesto


def bisiesto():
  anio = int(input("Escriba un año: "))
  if anio % 400 == 0 or (anio % 100 != 0 and anio % 4 == 0):
    print(f"El año {anio} es un año bisiesto.")
  else:
    print(f"El año {anio} no es un año bisiesto.")

bisiesto()

'''
'''
#Calculadora While
def Menu():
    print ("""************
    Calculadora
    ************
    Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir
    """)
  
def suma():
  a = float(input("Ingrese Primer Número a sumar\n"))
  b = float(input("Ingrese Segundo Número a sumar\n"))
  return a+b

def resta():
  c = float(input("Ingrese Primer Número a restar\n"))
  d = float(input("Ingrese Segundo Número a restar\n"))
  return c-d

def multiplicacion():
  e = float(input("Ingrese Primer Número a multiplicar\n"))
  f = float(input("Ingrese Segundo Número a multiplicar\n"))
  return e*f

def division():
  g = float(input("Ingrese Numerador\n"))
  h = float(input("Ingrese Denominador\n"))
  if h==0:
    print("Error, División entre 0")
  else:
    return g/h


def Calculadora():    
    Menu()
    opcion=0    
  
    while opcion != 5:  
      
      opcion = int(input("Selecione Opción\n"))     
    
      if (opcion==1):
          print ("La Suma es:", suma())
      elif(opcion==2):
          print ("La Resta es:", resta())
          
      elif(opcion==3):
          print ("La Multiplicación es:", multiplicacion())
          
      elif(opcion==4):
          print ("La División es:", division())

      elif(opcion == 5):
        print ("Gracias por usar la calculadora! bye!.")
        #break
        
      else:
        print ("Opción invalida intente de nuevo")


Calculadora()

'''

# Descuento While
def compra():
  total=0
  monto=float(input("Valor de la venta: $"))
  while monto!=0:
      if monto<0:
          print("Valor no válido.")
      else:
          total+=monto
      monto=float(input("Valor de la venta: $"))
  if total>1000000:
      total-=total*0.1
  print("Valor total a pagar: $", total)

compra()

