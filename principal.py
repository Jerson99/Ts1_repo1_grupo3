
import lib

#Probar posible números
capicuas = (
    123,
    122,
    121,
    12321,
    154123,
    15451,
)

for num in capicuas:
    if lib.capicua( num ):
        cap = 'Sí'
    else:
        cap = 'No' ;
    print( 'Número:', num, '- ¿Capicua?:', cap )

print( lib.es_primo( 12 ) )

n=int(input("ingrese un numero: "))
def evaluar_primo(n):
    contador=0
    resultado=True
    for i in range(1,n+1):
        if (n%i==0):
            contador+=1
        if (contador>2):
            resultado=False
            break
    return resultado
if (evaluar_primo(n)==True):
    print("el numero es primo")
else :
    print("el numero no es primo")

def factorial(num):
    fact = 1
    for i in range(1, num):
        fact += fact * i
    return fact
 
 
numero = int(input('Ingrese un numero'))
print('Su factorial es :', factorial(numero))
