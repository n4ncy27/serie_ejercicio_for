# EJERICIOS PARA TAREA
" serie: primero numeros primos "

n = int(input("Digite el numero que quieres generar: "))
s = "serie= "
for i in range(1, n-1):
        c = i 
        i = int((-(-1)**i + 6 * i +3)/2)
        if c == 1:
            s = s + "2,3,"
        if c == 2:
            s = s + str(i)
        else:
            s = s + str(i) + ","
print (s)
