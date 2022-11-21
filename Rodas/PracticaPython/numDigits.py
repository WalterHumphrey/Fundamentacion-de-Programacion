#Function that returns the number of digits of a integer

def numDigits(n):
    listN = [int(x) for x in n]
    
    print(len(listN), "digitos")

def main():
    num = input("Write an integer number:")
    numDigits(num)

if __name__ == "__main__":
    main()
