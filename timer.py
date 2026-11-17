import math
import time
from sense_hat import SenseHat

sense = SenseHat()

# Varje siffra är 3 pixlar bred och 5 pixlar hög
digits = {
    "0": ["111", "101", "101", "101", "111"],
    "1": ["010", "110", "010", "010", "111"],
    "2": ["111", "001", "111", "100", "111"],
    "3": ["111", "001", "111", "001", "111"],
    "4": ["101", "101", "111", "001", "001"],
    "5": ["111", "100", "111", "001", "111"],
    "6": ["111", "100", "111", "101", "111"],
    "7": ["111", "001", "010", "010", "010"],
    "8": ["111", "101", "111", "101", "111"],
    "9": ["111", "101", "111", "001", "111"],
}

def visa_tal(tal, farg):
    pixlar = [[0, 0, 0] for _ in range(64)]
    text = f"{tal:02d}"

    for plats, tecken in enumerate(text):
        x_start = plats * 4  # en tom kolumn mellan siffrorna

        for y, rad in enumerate(digits[tecken]):
            for x, pixel in enumerate(rad):
                if pixel == "1":
                    pixlar[(y + 1) * 8 + x_start + x] = farg

    sense.set_pixels(pixlar)

try:
    sekunder = int(input("Ange sekunder (1–99): "))

    if not 1 <= sekunder <= 99:
        raise ValueError("Ange ett tal mellan 1 och 99.")

    sluttid = time.monotonic() + sekunder
    senast_visad = None

    while True:
        kvar = max(0, math.ceil(sluttid - time.monotonic()))

        if kvar != senast_visad:
            farg = [255, 0, 0] if kvar <= 10 else [0, 255, 0]
            visa_tal(kvar, farg)
            senast_visad = kvar

        if kvar == 0:
            break

        time.sleep(0.05)

except KeyboardInterrupt:
    sense.clear()
