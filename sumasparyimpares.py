def suma_par_impar():
    lim = int(input("n: "))
    
    p = 0
    imp = 0
    
    for x in range(1, lim + 1):
        if x % 2 == 0:
            p += x
        else:
            imp += x
            
    print("suma de pares:", p)
    print("suma de impares:", imp)

suma_par_impar()
