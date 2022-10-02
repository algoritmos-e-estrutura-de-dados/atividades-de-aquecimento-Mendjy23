a = float(input())
b = float(input())
c = float(input())
pi = 3.14159

def triangulo_retangulo():
    area = (a*c)/2
    area = round(area, 3)
    return area
    

def raio_circulo():
    area = (c*c)*pi
    area = round(area, 3)
    return area

def area_trapezio():
    area = ((a + b)*c)/2
    area = round(area, 3)
    return area

def area_quadrado():
    area = b*b
    area = round(area, 3)
    return area

def area_retangulo():
    area = a*b
    area = round(area, 3)
    return area

print('TRIANGULO:',triangulo_retangulo(), '\nCIRCULO:',raio_circulo() ,'\nTRAPEZA:',area_trapezio(), '\nQUADRADA:',area_quadrado(), '\nRETANGLO',area_retangulo())
