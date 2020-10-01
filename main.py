import keyboard
import time
import keyboard
vaccinator = False
currentlySwitching = False
resistance = 0
print("running")
def reset():
    global vaccinator
    global resistance
    vaccinator = False
    resistance = 0
    print("reset")
def unequip():
    global vaccinator
    print("unequip")
    vaccinator = False

def cycleToResistance(newResistance): 
    print('cycleToResistance({})'.format(newResistance))
    global vaccinator
    global resistance
    global currentlySwitching
    if not currentlySwitching:
        if not vaccinator:
            currentlySwitching = True
            keyboard.press('2')
            time.sleep(0.004)
            keyboard.release('2')
            time.sleep(0.67)
            vaccinator = True
            currentlySwitching = False
        print (newResistance)
        print(resistance)
        while resistance != newResistance:
            resistance += 1  
            resistance %= 3
            keyboard.press('b')
            time.sleep(0.08)
            keyboard.release('b')
            time.sleep(0.035)

keyboard.on_press_key('F6',  lambda x: cycleToResistance(0))
keyboard.on_press_key('F8',  lambda x: cycleToResistance(1))
keyboard.on_press_key('F7',  lambda x: cycleToResistance(2))
keyboard.on_press_key('F4',  lambda x: unequip())
keyboard.on_press_key('F3',  lambda x: unequip())
keyboard.on_press_key('+', lambda x: reset())
keyboard.wait()
