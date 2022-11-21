def reverse(astring):
    newList = []
    for i in range(len(astring)):
        newList = [i] + newList

    newStr = ""
    for j in range(len(newList)):
        newStr = newStr + str(newList[j])
    print(newStr)

def main():
    num = "02468"
    numList = [int(x) for x in num]
    print(num)
    reverse(numList)

if __name__ == "__main__":
    main()