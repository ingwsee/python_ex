def isPrime(num):
    for i in range (2, float, (1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True
    
    for i in range (1, 20):
        if isPrime (i + 1):
            print (i + 1, end = " ")
    print ()
isPrime(5)
