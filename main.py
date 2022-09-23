print ('\033[1m'"1) Indica un ejemplo de un tipo de dato:\n"'\033[0m')
print("  a) Entero ")
print("Aquellos números que no incluyen decimales")
a=int(93) #"a" toma el valor de 93 parra ahorrar tiempo si lo tenemos que usar más de una vez
print(a)
print("  \n") #interlineado
print("  b) flotante")
print("Los datos flotantes, también conocidos como decimales, son aquellos que pertenecen al conjunto de los números reales, es decir, los que tienen parte decimal, además de la entera")
f=984.8 #f toma el valor de 984.8
print(f) 
print("\n")
print("  c) string")
print("Las cadenas permiten acumular diferentes caracteres, ya sean números, letras o por ejemplo, comillas")
s="Esta cadena contiene números (145), letras y comillas \" "
print(s)
print("\n")
print("  d) booleano")
print("Un booleano es un tipo de dato en el que se pueden almacenar dos valores, True o False")
c=6
d=3
if c > d: print("6 es mayor que 3") #si hubiera puesto c<d, no hubiera aparecido la frase
print("Otro ejemplo")
print(8<4) #para indicar si es verdadera o falsa la ecuación
print("\n")
print("\n")

print('\033[1m'" 2) Crea dos variables que se llamen nombre y apellido, en ellas introduce tu nombre y apellidos y luego prueba lo siguiente e indica el resultado:\n"'\033[0m')
Nombre= "Cristina"
Apellido= "Suárez"
print("  a)nombre + apellido")
print (Nombre + Apellido) # Para que lleve a cabo la fórmula no se ponen comillas, sino, escribiría directamente Nombre+Apellido, en vez del Nombre Completo
print("  b) nombre+apellido+.")
print(Nombre+Apellido+".")
print("  c) nombre*3")
print(Nombre*3)
print("\n")
print('\033[1m' "3) Retoma el ejercicio anterior, crea una variable que se llame nombreCompleto que una tu nombre y tu apellido con un espacio en el medio. Sobre esta variable, ¿eres capaz a extraer tu nombre utilizando slicing?"'\033[0m')
nombreCompleto="Cristina Suárez"
print(nombreCompleto)
print(nombreCompleto[:8]+nombreCompleto[-7:]+ nombreCompleto[-6:0]) #[x:x] sirve para indicar cuál parte quieres que se escriba, si pones la primera x en negativo empieza a contar desde atrás