def invertir():
    num = int(input("numero: "))
    neg = False
    
    if num < 0:
        neg = True
        num = abs(num)
        
    inv = 0
    while num > 0:
        res = num % 10
        inv = (inv * 10) + res
        num = num // 10
        
    if neg:
        inv = inv * -1
        
    print("resultado:", inv)

invertir()
