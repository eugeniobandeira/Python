import math
repeticao = 50 * "*"
print(repeticao)
print('Vamos relembrar a formula de Bhaskara')
print(repeticao)
print('Delta = "ax2 + bx + c = 0')
a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))
delta = b * b -4 * a * c
print((f'Delta: {delta:.2f}'))
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'O valor de x1 é {x1:.2f}')
    print(f'O valor de x2 é {x2:.2f}')
elif delta == 0:
    x = (-b + math.sqrt(delta)) / 2 * a
    print(f'O valor de x é {x:.2f}')
else:
    print("Não há raiz negativa.")


