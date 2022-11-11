from microbit import *

def dis_num(num,sel):
    number = num.split(":")
    for y in range(5):
        for i in range(2):
            if i < 1:
                if sel == 1:
                    display.set_pixel(3, y,int(number[0][y]))
                else:
                    display.set_pixel(0, y,int(number[0][y]))
            else:
                if sel == 1:
                    display.set_pixel(4, y,int(number[1][y]))
                else:
                    display.set_pixel(1, y,int(number[1][y]))

def main():
    seg = 0
    m = 0
    h = 0
    cont = 0
    cont2 = 0

    zero = "99999:99999"
    one = "00000:99999"
    two = "90999:99909"
    three = "90909:99999"
    four = "99900:09999"
    five = "99909:90999"
    six = "99999:90999"
    seven = "90900:99999"
    eight = "99099:99099"
    nine = "99900:99999"
    null = "00000:00000"
    fonts = (zero, one, two, three, four, five, six, seven, eight, nine)

    while True:
        for element in fonts:
            dis_num(element,1)
            if cont > 9:
                if seg % 10 == 0:
                    cont2 += 1
                    if cont2 > 5:
                        cont2 = 0
                dis_num(fonts[cont2],2)
            else:
                dis_num(null,2)
            if seg == 60:
                seg = 0
                m +=1
                if m == 60:
                    m = 0
                    h += 1
                    if h == 24:
                        h = 0
            if button_a.is_pressed():
                dis_num(fonts[m],1)
                #if seg % 10 == 0:
                dis_num(null,2)

            print("seg: ",seg)
            print("min: ",m)
            print("hor: ",h)
            sleep(1000)
            seg += 1
            cont += 1
            if cont == 60:
                cont = 0


if __name__ == "__main__":
    main()
