#1
'''
2012 es bisiesto
2010 no es bisiesto
2000 es bisiesto
1900 no es bisiesto
'''


def bisiesto():
  anio = int(input("Escriba un año: "))
  if anio % 400 == 0 or (anio % 100 != 0 and anio % 4 == 0):
    print(f"El año {anio} es un año bisiesto.")
  else:
    print(f"El año {anio} no es un año bisiesto.")

bisiesto()