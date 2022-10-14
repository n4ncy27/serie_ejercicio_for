# SERIE = 1,4,9,16,25,36,49- ponerles cuantos digitos tiene la serie"

n = int(input("Digite el valor de n: "))
s="serie: "
for i in range(1, n+1):
    t= 1*i
    if i < n:
        s=s+str(i)+","
    else:
        s=s+str(i)
print(s)
