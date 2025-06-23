from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
mouse.position = (2559, 200)

c3 = 0
c4=0
mouse.press(Button.left)
while True:
    mouse.move(-1, 0)
    c3 += 1
    if c3 > 2559:
        c3 = 0
        mouse.move(2559, 3)
        c4+=1
    if c4>210:
        c4=0
        mouse.position = (2559, 200)
    if keyboard.is_pressed('f1'):
        break
