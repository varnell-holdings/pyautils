import pyautogui as pya
import time
import sys

def get_color(x, y):
    time.sleep(5)
    im = pya.screenshot()
    pix = im.getpixel((x, y))
    return pix

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(get_color(x, y))
