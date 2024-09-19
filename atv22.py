# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
soma = 0 
while True:
    numero = float(input("coloque qualquer valor ou coloque 0 para fehar o programa."))
    soma+=numero
    if numero == 0:
        break
print(f"o resultado dara{soma}")