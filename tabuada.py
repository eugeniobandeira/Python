#tabuada = (input('quer a tabuada de qual número? '))
#for elemento in range(11):
    #print(tabuada, ' X ', elemento, '= ', int(elemento) * int(tabuada))

print('--------------')

tab = input('quer a tabu de qual nume? ')
limite = int(input('qual vai ser o limite? '))
contador = 0
while contador <= limite:
    print(tab, ' x ', contador, ' = ', int(tab) * contador)
    contador = contador + 1