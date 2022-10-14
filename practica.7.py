"""Generar la siguiente serie 3,8,13,18,23,28...n"""

#Entrada
n = int(input("Digite el valor de n: "))

#Proceso
s = "Serie: "
for i in range (1,n+1): 
    t = t = 5*i - 2
    
    if i < n:
        s = s + str(t) + ", "
    else:
        s = s + str(t)

#Salida
print("--- Resultado ---")
print(s)