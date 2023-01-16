from microbit import *
import gigglebot

def giggle_forward(d, speed):
    gigglebot.set_speed(speed, speed)
    speed_to_cm_s = speed * 0.46
    time = d/speed_to_cm_s
    ms_offset = 150
    gigglebot.drive(gigglebot.FORWARD, time*1000 + ms_offset)

def giggle_turn(degrees, side, speed):
    if side == "left":
        gigglebot.set_speed(speed, -speed)
    elif side == "right":
        gigglebot.set_speed(-speed, speed)

    radians = degrees * (3.14/180)
    radians_sec = speed * 0.07283185
    time = radians / radians_sec
    ms_offset = 5

    gigglebot.drive(gigglebot.FORWARD, time * 1000 + ms_offset)
    gigglebot.set_speed(speed, speed)

def giggle_polygon(n, size, speed):
    for _ in range(n):
        giggle_forward(size, speed)
        giggle_turn(360 // n, "left", speed)

def main():
    sleep(1000)
    giggle_polygon(50, 2, 70)

if __name__ == "__main__":
    main()
