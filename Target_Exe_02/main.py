n = int(input("Digite um número: "))

anterior = 0
proximo = 0

while(proximo < n):
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior
  if proximo == 0:
    proximo = proximo + 1

if n == proximo:
    print(n, "Faz parte da sequência de Fibonnaci.")
else:
    print(n, "Não faz parte da sequência de Fibonnaci.")