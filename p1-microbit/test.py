def main():
    s = 0
    h = 0
    m = 0
    
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
    fonts = (zero, one, two, three, four, five, six, seven, eight, nine)
    
    while True:
        for n in range(10):
            number = fonts[n].split(":")
            for y in range(5):
                for i in range(2):
                    if i < 1:
                        x = 3
                    else:
                        x = 4
                    #display.set_pixel(x, y,9)
        
        #sleep(1000)

if __name__ == "__main__":
    main()