def is_prime(num):
    for n in range(2, num):
        print(num % n)        
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def main():
    val = int(input("Ingrese un numero para saber si es primo:"))
    print(is_prime(val))

if __name__ == "__main__": #Correr el programa principal
    main()   