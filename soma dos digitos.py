numero = int(input("Digite um número inteiro positivo: "))

soma_digitos = 0

# Enquanto o número for maior que 0, continuamos a somar os dígitos
while numero > 0:
    # Adicionamos o último dígito ao total da soma
    soma_digitos += numero % 10
    # Removemos o último dígito do número
    numero //= 10

print("A soma dos dígitos do número é:", soma_digitos)

