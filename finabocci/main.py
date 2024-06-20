while True:

    def calcular_fibonacci(n):
        if n <= 1:
            return n
        else:
            return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

    print("Sequências de Fibonacci do valor informado.")
    n = int(input("Informe um número:"))

    for x in range(n):
        print(calcular_fibonacci(x))