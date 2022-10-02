dist = float(input('distancia:'))
comb = float(input('combustivel gasto:'))

resultado = dist/comb
resultado = round(resultado, 3)

print(resultado, 'km/l')