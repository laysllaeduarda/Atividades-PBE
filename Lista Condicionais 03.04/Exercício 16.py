num = int(input("Digite um número:"))

if num < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo")
elif num > 100:
    print("O número inserido é muito grande, por favor, reduza para um valor abaixo de 100")
else:
    resultado = num**0.5
    print(f"Raiz quadrada: {resultado}")
