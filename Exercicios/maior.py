a = int(input())
b = int(input())
c = int(input())

maior = ((a-b)*(a*b*c) + a + b)
maiorAB = maior/2

if (a> b) and (a>c):
    maior1 = a
elif (b>a) and (b>c):
       maior1 = b
elif (c> a) and (c>b):
     maior1 = c


print(maior1, 'eh o maior')