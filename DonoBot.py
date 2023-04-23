import PIL
import pyautogui
import win32api
import time
from mss import mss
import numpy
import pyscreenshot as ImageGrab

monitor = mss().grab(mss().monitors[1])

x1 = int(monitor.width * (805 / 1920))
x2 = int(monitor.width * (940 / 1920))
troopY = int(monitor.height * (244 / 1080))
spellY = int(monitor.height * (647 / 1080))
troopPixel = ((int(monitor.width * (836 / 1920)), int(monitor.height * (308 / 1080))), (61, 121, 181))
spellPixel = ((int(monitor.width * (835 / 1920)), int(monitor.height * (727 / 1080))), (109, 69, 189))
donoPixel = ((int(monitor.width * (610 / 1920)), int(monitor.height * (896 / 1080))), (123, 196, 46))
nextPixel = ((int(monitor.width * (727 / 1920)), int(monitor.height * (926 / 1080))), (145, 200, 14))
upPixel = ((int(monitor.width * (728 / 1920)), int(monitor.height * (127 / 1080))), (156, 209, 13))
screenPixel = ((int(monitor.width * (851 / 1920)), int(monitor.height * (787 / 1080))), (255, 255, 255))
errorPixel = ((int(monitor.width * (785 / 1920)), int(monitor.height * (428 / 1080))), (66, 66, 66))
mainScreenPixel = ((int(monitor.width * (22 / 1920)), int(monitor.height * (524 / 1080))), (197, 81, 21))
scrollPixel = ((int(monitor.width * (661 / 1920)), int(monitor.height * (591 / 1080))), (169, 169, 169))
trainTroopPixel = ((int(monitor.width * (463 / 1920)), int(monitor.height * (43 / 1080))), (250, 250, 248))
brewSpellPixel = ((int(monitor.width * (791 / 1920)), int(monitor.height * (35 / 1080))), (248, 248, 248))
buildSiegePixel = ((int(monitor.width * (1115 / 1920)), int(monitor.height * (80 / 1080))), (233, 236, 227))
reconnectPixel = ((int(monitor.width * (606 / 1920)), int(monitor.height * (1014 / 1080))), (116, 189, 47))
crashPixel = ((int(monitor.width * (1730 / 1920)), int(monitor.height * (153 / 1080))), (255, 201, 52))

troopQueue = []
darkQueue = []
spellQueue = []
siegeQueue = []

troopValues = [
    [187.11851851851853, 153.38518518518518, 103.87407407407407],
    [166.7037037037037, 117.66666666666667, 134.0074074074074],  
    [197.76296296296297, 138.95555555555555, 99.3037037037037],  
    [123.74814814814815, 151.0074074074074, 109.9037037037037],  
    [103.27407407407408, 109.38518518518518, 108.00740740740741],
    [150.2, 165.65925925925927, 168.2074074074074],
    [135.57777777777778, 144.11851851851853, 154.45925925925926],
    [200.84444444444443, 178.13333333333333, 167.01481481481483],
    [137.33333333333334, 121.92592592592592, 157.9111111111111], 
    [85.62962962962963, 99.32592592592593, 143.37777777777777],  
    [140.84444444444443, 143.2962962962963, 129.36296296296297], 
    [158.38518518518518, 143.83703703703705, 137.42962962962963],
    [70.82222222222222, 97.25185185185185, 154.13333333333333],  
    [147.4962962962963, 154.06666666666666, 190.4962962962963],  
    [81.95555555555555, 139.05925925925925, 176.74814814814815],
    [110.21481481481482, 119.27407407407408, 125.02222222222223],
    [191.15555555555557, 125.2074074074074, 103.67407407407407], 
    [143.11111111111111, 129.8074074074074, 121.47407407407407], 
    [129.62222222222223, 129.38518518518518, 159.3925925925926],
    [127.27407407407408, 106.12592592592593, 95.63703703703703],
    [105.42222222222222, 108.36296296296297, 211.36296296296297],
    [162.63703703703703, 167.06666666666666, 169.5851851851852],
    [118.56296296296296, 117.5037037037037, 118.24444444444444], 
    [182.42962962962963, 108.4962962962963, 95.18518518518519],  
    [152.86666666666667, 134.22222222222223, 145.15555555555557],
    [136.78518518518518, 124.34814814814816, 122.05925925925926],
    [108.67407407407407, 98.45185185185186, 97.73333333333333]
]

spellValues = [
    [112.00740740740741, 219.0, 247.71851851851852],
    [230.17037037037036, 206.33333333333334, 143.59259259259258],
    [177.34814814814814, 151.44444444444446, 206.6888888888889],
    [192.82962962962964, 232.28148148148148, 123.34074074074074],
    [155.3111111111111, 234.85185185185185, 246.97037037037038],
    [227.17037037037036, 159.6888888888889, 98.14814814814815],
    [119.57777777777778, 101.08888888888889, 84.25925925925925],
    [227.61481481481482, 165.88148148148147, 206.1925925925926],
]

troopKeys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r"]
darkKeys = ["9", "0", "q", "w", "e", "r", "t", "y"]
spellKeys = ["1", "2", "3", "4", "5", "9", "0", "q"]
siegeKeys = ["1", "5", "9", "e", "t"]

wait = float(input("Wait time:"))
diff = float(input("Diff:"))

def main():
    print("Started")
    doDonos()
    #mouseCoords()

def pressKey(key, error = False):
    if not doPixelsMatch(errorPixel) or error:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
        time.sleep(wait)

def doDonos():
    time.sleep(10)
    while True:
        if doPixelsMatch(mainScreenPixel) and not doPixelsMatch(errorPixel):
            pressKey("`")
            pressKey("z")
            while doPixelsMatch(upPixel):
                pressKey("x")
            pressKey("c")
            while doPixelsMatch(nextPixel):
                pressKey("v")
                donate()
            pressKey("m")
            if len(troopQueue) > 0 or len(darkQueue) > 0 or len(spellQueue) > 0 or len(siegeQueue) > 0:
                trainTroops()
        else:
            if doPixelsMatch(reconnectPixel):
                print("ok")
                pressKey("v", True)
                pressKey("/", True)
            elif doPixelsMatch(crashPixel):
                pressKey("k", True)
            else:
                pressKey("l", True)
            pressKey("e", True)
            pressKey("z", True)
            pressKey("m", True)
            time.sleep(wait)

def donate():
    while doPixelsMatch(donoPixel):
        pressKey("b")
        if not doPixelsMatch(troopPixel) and not doPixelsMatch(spellPixel) and doPixelsMatch(screenPixel) and not doPixelsMatch(errorPixel):
            pressKey("b")
            break
        while doPixelsMatch(troopPixel) and not doPixelsMatch(errorPixel) and doPixelsMatch(screenPixel):
            troop = getCard(getRGB(troopY), troopValues)
            if troop < 14:
                troopQueue.append(troop)
            elif troop >= 22:
                siegeQueue.append(troop)
            else:
                darkQueue.append(troop)
            pressKey("n")
        while doPixelsMatch(spellPixel) and not doPixelsMatch(errorPixel) and doPixelsMatch(screenPixel):
            spell = getCard(getRGB(spellY), spellValues)
            spellQueue.append(spell)
            pressKey(",")
        if doPixelsMatch(screenPixel):
            pressKey("b")

def trainTroops():
    pressKey("a")
    pressKey("s")
    while len(troopQueue) > 0 and not doPixelsMatch(errorPixel) and not doPixelsMatch(scrollPixel) and doPixelsMatch(trainTroopPixel):
        pressKey(troopKeys[troopQueue[0]])
        troopQueue.pop(0)
    pressKey("tab")
    while len(darkQueue) > 0 and not doPixelsMatch(errorPixel) and doPixelsMatch(scrollPixel) and doPixelsMatch(trainTroopPixel):
        pressKey(darkKeys[darkQueue[0] - 14])
        darkQueue.pop(0)
    pressKey("d")
    while len(spellQueue) > 0 and not doPixelsMatch(errorPixel) and doPixelsMatch(brewSpellPixel):
        pressKey(spellKeys[spellQueue[0]])
        spellQueue.pop(0)
    pressKey("f")
    while len(siegeQueue) > 0 and not doPixelsMatch(errorPixel) and doPixelsMatch(buildSiegePixel):
        pressKey(siegeKeys[siegeQueue[0] - 22])
        siegeQueue.pop(0)
    pressKey("z")

def doPixelsMatch(pixel):
    image = ImageGrab.grab(bbox=(pixel[0][0], pixel[0][1], pixel[0][0] + 1, pixel[0][1] + 1))
    difference = numpy.subtract(image.getpixel((0, 0)), pixel[1])
    difference = numpy.absolute(difference)
    difference = numpy.sum(difference)
    if difference < diff:
        return True
    else:
        return False

def getRGB(y):
    pixels = ImageGrab.grab(bbox=(x1, y, x2, y + 1))
    return numpy.mean(pixels, axis=1)

def getCard(rgb, values):
    differences = []
    for value in values:
        difference = numpy.subtract(rgb, value)
        difference = numpy.absolute(difference)
        difference = numpy.sum(difference)
        differences.append(difference)
    return differences.index(min(differences))

def mouseCoords():
    while win32api.GetKeyState(0x1B) >= 0:
        if win32api.GetKeyState(0x02) < 0:
            print(str(pyautogui.position()) + " " + str(PIL.ImageGrab.grab().load()[pyautogui.position().x, pyautogui.position().y]))
        time.sleep(0.1)

def getValue(y):
    values = ""
    while win32api.GetKeyState(0x1B) >= 0:
        if win32api.GetKeyState(0x02) < 0:
            rgb = getRGB(y)
            print(rgb)
            values += "[" + str(rgb[0]) + ", " + str(rgb[1]) + ", " + str(rgb[2]) + "],\n"
        time.sleep(0.1)
    print(values)

main()