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
