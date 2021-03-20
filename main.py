import keyboard
import time
import keyboard
print("running")
class vacc_model:
    def __init__(self):
        self.reset()
    def reset(self):
        self.vaccinator = False
        self.resistance = 0
    def unequip(self, key):
        self.vaccinator = False
        keyboard.press(key)
        time.sleep(0.03)
        keyboard.release(key)
    def cycleToResistance(self, newResistance): 
        iters = 0
        while self.resistance != newResistance:
            self.resistance = (self.resistance + 1) % 3
            iters += 1
        if not self.vaccinator:
            self.vaccinator = True
            keyboard.press('2')
            time.sleep(0.015)
            keyboard.release('2')
            time.sleep(0.75)
        for i in range(iters):
            keyboard.press('b')
            time.sleep(0.03)
            keyboard.release('b')
            time.sleep(0.07)

vm = vacc_model()
keyboard.on_press_key('g',  lambda x: vm.cycleToResistance(0))
keyboard.on_press_key('F8',  lambda x: vm.cycleToResistance(1))
keyboard.on_press_key('F7',  lambda x: vm.cycleToResistance(2))
keyboard.on_press_key('o',  lambda x: vm.unequip("l"))
keyboard.on_press_key('p',  lambda x: vm.unequip("k"))
keyboard.on_press_key('6', lambda x: vm.reset())
keyboard.wait()
