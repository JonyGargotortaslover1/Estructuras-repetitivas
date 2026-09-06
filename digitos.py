def digitos():
    n = int(input("ingresa un numero: "))
    n = abs(n)
    
    c = 0
    if n == 0:
        c = 1
    else:
        while n > 0:
            n = n // 10
            c = c + 1
            
    print("cantidad de digitos:", c)

digitos()
