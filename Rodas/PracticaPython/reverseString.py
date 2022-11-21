def reverse(astring):
    newList = []
    for i in range(len(astring)):
        newList = [i] + newList
    print(newList)

def main():
    num = "02468"
    numList = [int(x) for x in num]
    print(numList)
    reverse(numList)

if __name__ == "__main__":
    main()