
a = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão: "))
n = int(input("Digite o número de termos: "))

#calc progressao
pg = [a * r**(i - 1) for i in range(1, n + 1)]

print("Progressão Geométrica ({} termos):".format(n))
print(pg)
