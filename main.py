from PIL import Image, ImageGrab
import pyautogui
import time

# link: https://www.doc88.com/p-99829253207693.html?r=1
time.sleep(5)
# using the grab method

for i in range(302):
    dino = ImageGrab.grab(bbox=(600, 10, 1280, 1050))
    dino.save(f"page_added_{234+ i}.png")
    pyautogui.scroll(-790)
    time.sleep(2)
# dino.show()

