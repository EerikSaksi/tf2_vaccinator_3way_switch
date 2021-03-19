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
        self.currentlySwitching = False
    def unequip(self):
        print("unequip")
        self.vaccinator = False
    def cycleToResistance(self, newResistance): 
        print('cycleToResistance({})'.format(newResistance))
        if not self.currentlySwitching:
            if not self.vaccinator:
                self.currentlySwitching = True
                keyboard.press('2')
                time.sleep(0.015)
                keyboard.release('2')
                time.sleep(0.75)
                self.vaccinator = True
                self.currentlySwitching = False
            while True:
                if self.resistance == newResistance:
                    break
                keyboard.press('b')
                time.sleep(0.03)
                keyboard.release('b')
                self.resistance += 1  
                self.resistance %= 3
                if self.resistance != newResistance:
                    time.sleep(2)

vm = vacc_model()
keyboard.on_press_key('g',  lambda x: vm.cycleToResistance(0))
keyboard.on_press_key('F8',  lambda x: vm.cycleToResistance(1))
keyboard.on_press_key('F7',  lambda x: vm.cycleToResistance(2))
keyboard.on_press_key('o',  lambda x: vm.unequip())
keyboard.on_press_key('p',  lambda x: vm.unequip())
keyboard.on_press_key('6', lambda x: vm.reset())
keyboard.wait()
