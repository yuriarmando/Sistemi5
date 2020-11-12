a=int(input('Inserisci il primo numero: '))
b=int(input('Inserisci il secondo numero: '))

while b>0:
    r=a%b
    a,b=b,r

print(a)