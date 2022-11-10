from microbit import *

MAX = 10

def main():
    readings = [(0, 0, 0)] * MAX
    ax = [0] * MAX
    ay = [0] * MAX
    az = [0] * MAX
    j = 0
    while True:
        for i in range(MAX):
            j = j + 1
            readings[i] = accelerometer.get_values()
            ax[i] = readings[i][0]
            ay[i] = readings[i][1]
            az[i] = readings[i][2]
            if j < MAX:
                meanx = sum(ax) / j
                meany = sum(ay) / j
                meanz = sum(az) / j
            else:
                meanx = sum(ax) / MAX
                meany = sum(ay) / MAX
                meanz = sum(az) / MAX
            print( (meanx,meany,meanz) )
            if button_a.is_pressed():
                max_r = "Max x: " + str(max(ax)) + "Max y: " + str(max(ay)) + "Max z: " + str(max(az))
                display.scroll(max_r)
            if button_b.is_pressed():
                min_r = "Min x: " + str(min(ax)) + "Min y: " + str(min(ay)) + "Min z: " + str(min(az))
                display.scroll(min_r)
        sleep(200)

if __name__ == "__main__":
    main()
