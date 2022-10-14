# serie 1/3, 2/5, 9/7, 64/9,1/26


"Generar la siguiente serie1/3, 2/5, 9/7, 64/9,1/26..... n"
n = int(input("Digite el valor de n: "))
s = "series: "
for i in range(1, n+1):
    t = (i*i)+1
    
    if i < n:
        s = s + "1/"+ str(t) + " , "
    else:
        s = s +"1/" + str(t)

print("---------RESULTADO-------------")
print(s)