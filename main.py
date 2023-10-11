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
'''
'''
#adivinar mejorado
import random

def adivinaFeature()  :

  numero_secreto = random.randint(1, 100)
  intentos = 0
  max_intentos = 5
  
  while intentos < max_intentos:
      intento = int(input("Adivina el número: "))
      intentos += 1
      if intento == numero_secreto:
          print("¡Correcto! Has adivinado el número en", intentos, "intentos.")
          break
      elif intento < numero_secreto:
          print("El número es mayor.")
      else:
          print("El número es menor.")
  else:
      print("Agotaste tus", max_intentos, "intentos. El número secreto era", numero_secreto)

adivinaFeature()
'''

'''
#caracteres
def Impcaracter():
  cadena = input("Ingrese una palabra o frase: ")
  
  for caracter in cadena:
      print(caracter)

Impcaracter()
'''
'''
#Factorial
def factorial():
  numero = int(input("Ingrese un número: "))
  factorial = 1
  
  for i in range(1, numero + 1):
      factorial *= i

  print("El factorial de", numero, "es", factorial)

factorial()
'''
'''
#tabla de multiplicar
def tablaM():
  n = int(input("Ingrese un número: "))
  
  for i in range(1, 11):
      resultado = n * i
      print(n, "x", i, "=", resultado)

tablaM()
'''
'''
#adivinar número
import random
def adivina():
  numero_secreto = random.randint(1, 100)
  adivinado = False
  
  while not adivinado:
      intento = int(input("Adivina el número: "))
      if intento == numero_secreto:
          print("¡Correcto! Has adivinado el número.")
          adivinado = True
      elif intento < numero_secreto:
          print("El número es mayor.")
      else:
          print("El número es menor.")

adivina()
'''
'''
#Triqui
def inicializar_tablero():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    return tablero

def imprimir_tablero(tablero):
    filaT=0
    for fila in tablero:
        filaT=filaT+1
        print("|".join(fila))
        if filaT <= 2:
           print("-" * 5)

def realizar_jugada(tablero, jugador, fila, columna):
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador
        return True
    else:
        return False

def verificar_estado(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]
    
    # Verificar empate
    empate = all(tablero[i][j] != ' ' for i in range(3) for j in range(3))
    if empate:
        return 'Empate'
    
    return None

def jugar_triqui():
    tablero = inicializar_tablero()
    jugador_actual = 'X'
    
    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        
        fila = int(input("Ingrese el número de fila (0, 1, o 2): "))
        columna = int(input("Ingrese el número de columna (0, 1, o 2): "))
        
        if realizar_jugada(tablero, jugador_actual, fila, columna):
            estado = verificar_estado(tablero)
            
            if estado:
                imprimir_tablero(tablero)
                if estado == 'Empate':
                    print("¡Es un empate!")
                else:
                    print(f"¡El jugador {estado} ha ganado!")
                break
            
            if jugador_actual == 'X':
              jugador_actual = 'O' 
            else: 
              jugador_actual= 'X'

jugar_triqui()
#Listas
def listas1():
  lista=[]
  lista2=[]
  
  for i in range(1,6):
    lista.append(input("Ingrese una cadena: "))
    
  lista2= lista.copy()
  lista2.reverse()
  
  for j in lista2:
    print(j)

listas1()


import random
def lista2():
  lista_numeros = []
  
  for indice in range(1,11):
  	lista_numeros.append(random.randint(1,10))
  
  for numero in lista_numeros:
  	print("Para el número",numero," su cuadrado es: ",numero ** 2," y su cubo es: ",numero ** 3)

lista2()


def notasLista():
  notas = []
  for indice in range(1,6):
  	while True:
  		nota = int(input("Introduce la nota: "))
  		if nota>=0 and nota<=10: break
  	notas.append(nota)
  
  print("Notas: ")  
  for nota in notas:
  	print(nota)
    
  print()
  print("Nota media: ",sum(notas)/len(notas))
  print("Nota max: ",max(notas))
  print("Nota min: ",min(notas))

notasLista()

def listaNumbers():
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for i in range(1, 11):
      print(numbers[-i], end=", ")
 
  #numbers.reverse()
  #for number in numbers:
  #  print(number, end=", ")
listaNumbers()

def materiasL():
  materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
  for i in range(len(materias)-1, -1, -1):
      nota = float(input("¿Qué nota has sacado en " + materias[i] + "? "))
      if nota >= 3:
          materias.pop(i)
  print("Tienes que repetir " + str(materias))

materiasL()

def letasL():
  alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for i in range(len(alfabeto), 1, -1):
      if i % 3 == 0:
          alfabeto.pop(i-1)
  print(alfabeto)

letasL()

def palindromo():
  palabraIng = input("Introduce una palabra: ")
  palabra = palabraIng.lower()
  palabra_inv = palabra.lower()
  word = list(palabra)
  palabra_inv = list(palabra_inv)
  palabra_inv.reverse()
  if word == palabra_inv:
      print("Es un palíndromo")
  else:
      print("No es un palíndromo")

palindromo()

def menu():
  print ("""************
Lista de Contactos
************
Menu
1) Crear Contacto
2) Buscar Contacto
3) Eliminar Contacto
4) Mostrar Contactos
5) Salir
""")

def agregar_contacto(nombre, telefono, correo, contactos):
    contacto = [nombre, telefono, correo]
    contactos.append(contacto)

def buscar_contacto(nombre,contactos):
  for contacto in contactos:
    if contacto[0] == nombre:
        print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}")

def elimina_contacto(nombre,contactos):
  for contacto in contactos:
    if contacto[0] == nombre:
      contactos.pop(contactos.index(contacto))

  #print(contactos)

def Lista_contactos():
  contactos = []
  menu()
  opcion=0
  while opcion!=5:
    opcion= int(input("Selecione Opción\n"))

    if opcion == 1:
      nombrec=input("Escribe el nombre del contacto: ")
      telefonoc=input("Escribe el teléfono del contacto: ")
      correoc=input("Escribe el email del contacto: ")
      agregar_contacto(nombrec, telefonoc, correoc, contactos)

    elif opcion == 2:
      nombreb=input("Escriba el nombre del contacto que desea buscar: ")
      buscar_contacto(nombreb,contactos)

    elif opcion==3:
      nombreE=input("Escriba el nombre del contacto a eliminar: ")
      elimina_contacto(nombreE,contactos)
      
    elif opcion==4:
      print("Los contactos son: ", contactos)

    elif opcion==5:
      print("Gracias por usar la app!. bye")
      break
    
    else:
      print("Opción Invalida")
      
Lista_contactos()

import random

def juego_cartas():  
  palos = ["Corazones", "Diamantes", "Picas", "Tréboles"]
  valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  
  mazo = []
  
  for palo in palos:
      for valor in valores:
          carta = [valor, palo]
          mazo.append(carta)  
  
  random.shuffle(mazo)

  return mazo
  
def repartir_cartas(numero_jugadores, cartas_por_jugador):
    mazo= juego_cartas()
    jugadores = [[] for _ in range(numero_jugadores)]
    for _ in range(cartas_por_jugador):
        for jugador in jugadores:
            carta = mazo.pop()
            jugador.append(carta)

    for i, jugador in enumerate(jugadores):
        print(f"Jugador {i + 1}: {jugador}")

repartir_cartas(4,2)
  
#Ventas
def menu():
  print ("""************
Registrar Ventas
************
Menu
1) Crear venta
2) Mostrar Total ventas
3) Salir
""")
  
def registrar_venta(producto, cantidad, precio,ventas):
    venta = [producto, cantidad, precio]
    ventas.append(venta)

def ventas():
  opcion=0
  ventas = []
  menu()
  
  while opcion != 3:
    
    opcion= int(input("Selecione Opción\n"))
    
    if opcion==1:
      productov=input("Ingrese que producto vendio: ")
      cantidadv=int(input("Ingrese la cantidad de unidades vendidas: "))
      preciov=float(input("Ingrese el valor del producto: "))
    
      registrar_venta(productov, cantidadv, preciov,ventas) 
      
    elif opcion == 2:  
      total_ventas = sum(venta[1] * venta[2] for venta in ventas)
      print(f"Total de ventas diarias: ${total_ventas}")

    elif opcion == 3:
      print("Gracias por usar la aplicación. Bye!")
      break
    else:
      print("Opción invalida")

ventas()

#suma Matrices
def suma_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = suma_matrices(matriz1, matriz2)
print(resultado)

#Transpuesta Matrices
def matriz_transpuesta(matriz):
    transpuesta = []
    for j in range(len(matriz[0])):
        fila = []
        for i in range(len(matriz)):
            fila.append(matriz[i][j])
        transpuesta.append(fila)
    return transpuesta

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_transpuesta = matriz_transpuesta(matriz)
print(matriz_transpuesta)

#Multiplicar matrices
def multiplicar_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplicar_matrices(matriz1, matriz2)
print(resultado)

#maximo de matriz
def encontrar_maximo(matriz):
    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
maximo = encontrar_maximo(matriz)
print(maximo)

def producto_escalar(matriz, escalar):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz[i][j] * escalar
    
    return resultado

  
#diccionarios
#divisa
def divisaSimbol():
  monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
  moneda = input("Introduce una divisa: ")
  if moneda.title() in monedas:
      print(monedas[moneda.title()])
  else:
      print("La divisa no está.")

#numero al cuadrado llave
def numeroCuadrado():
  numero = int(input("Dime un número:"))
  cuadrados = {}
  
  for num in range(1,numero+1):
      cuadrados[num] = num ** 2
  for num, valor in cuadrados.items():
      print("%d -> %d" % (num,valor))

numeroCuadrado()

#repite cadena
def cadenaRep():
  dict = {}
  cadena = input("Dame una cadena:")
  for caracter in cadena:
  	if caracter in dict:
  		dict[caracter]+=1
  	else:
  		dict[caracter]=1	
  
  for campo,valor in dict.items():
  	print (campo,"->",valor)

cadenaRep()

#peso frutas
def precioF():
  frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
  fruta = input('¿Qué fruta quieres? ').title()
  kg = float(input('¿Cuántos kilos? '))
  if fruta in frutas:
      print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
  else: 
      print("Lo siento, la fruta", fruta, "no está disponible.")

precioF()

#cleintes diccionario
def clienteDic():
  clientes = {}
  opcion = ''
  while opcion != '6':
      if opcion == '1':
          cc = input('Introduce CC del cliente: ')
          nombre = input('Introduce el nombre del cliente: ')
          direccion = input('Introduce la dirección del cliente: ')
          telefono = input('Introduce el teléfono del cliente: ')
          email = input('Introduce el correo electrónico del cliente: ')
          vip = input('¿Es un cliente preferente (S/N)? ')
          cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
          clientes[cc] = cliente
      if opcion == '2':
          nif = input('Introduce CC del cliente: ')
          if nif in clientes:
              del clientes[cc]
          else:
              print('No existe el cliente con el cc', nif)
      if opcion == '3':
          nif = input('Introduce CC del cliente: ')
          if nif in clientes:
              print('CC:', cc)
              for clave, valor in clientes[cc].items():
                  print(clave.title() + ':', valor)
          else:
              print('No existe el cliente con el cc', cc)
      if opcion == '4':
          print('Lista de clientes')
          for clave, valor in clientes.items():
              print(clave, valor['nombre'])
      if opcion == '5':
          print('Lista de clientes preferentes')
          for clave, valor in clientes.items():
              if valor['preferente']:
                  print(clave, valor['nombre'])
      opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferencial\n(6) Terminar\nElige una opción:')

clienteDic()
'''
