import pyautogui as mouse
from pyautogui import alert, screenshot, locateOnScreen, center
import keyboard
import sys
from time import sleep as wait
quant = int(input('quantas contas vc quer pegar? '))

def setup():
    def fake_click(posx, posy):
        mouse.moveTo(posx, posy, 0)
        mouse.keyDown('ctrl')
        mouse.click()
        mouse.keyUp('ctrl')

    def close_actual_tab():
        mouse.keyDown('ctrl')
        mouse.keyDown('w')
        mouse.keyUp('ctrl')
        mouse.keyUp('w')

    def move_and_click(posx, posy):
        mouse.moveTo(posx, posy, 0) 
        mouse.click()

    def copy():
        mouse.keyDown('ctrl')
        mouse.keyDown('c')
        mouse.keyUp('ctrl')
        mouse.keyUp('c')

    def paste():
        mouse.keyDown('ctrl')
        mouse.keyDown('v')
        mouse.keyUp('ctrl')
        mouse.keyUp('v')

    def reverify_captcha():
        im2 = screenshot('reverify.png', region=(987, 595, 5, 5))
        verify_loc = locateOnScreen('reverify.png')
        reverify = im2.getpixel((2, 2))
        if str(reverify) == '(255, 255, 255)':
            move_and_click(948, 609)
            wait(1)
            move_and_click(1007, 805)
            wait(5)
            reverify_captcha()
        else:
            pass


    move_and_click(345, 712)

    for i in range(0, quant):
        if keyboard.is_pressed('e'):
            sys.exit()

        wait(3)
        fake_click(363, 664)
       

        move_and_click(913, 16)
        
        wait(4)
        move_and_click(823, 476)
        
        wait(1)
        im2 = screenshot('verify.png', region=(1070, 585, 120, 50))
        verify_loc = locateOnScreen('verify.png')
        color = im2.getpixel((5, 5))
        color2 = im2.getpixel((20, 0))
        if str(color) == '(74, 144, 226)':
            #audio captcha
            move_and_click(1007, 608)
            wait(5)
        elif str(color2) == '(245, 245, 245)':
            pass
        else:
            #img captcha
            move_and_click(1007, 805)
            wait(5)

        reverify_captcha()

        move_and_click(975, 566)

        wait(19)
        move_and_click(973, 794)

        wait(3)
        move_and_click(213, 166)

        mouse.tripleClick()
        copy()

        close_actual_tab()

        wait(1)
        move_and_click(146, 13)
        
        wait(1)
        move_and_click(1247, 255)
        mouse.keyDown('enter')
        mouse.keyUp('enter')
        paste()

        wait(1)
        move_and_click(657, 14)

        wait(1)
        move_and_click(369, 737)

        

wait(3)
setup()

alert(title='FARMING CONCLUIDA:', text = f'VOCÊ PEGOU {quant} CONTAS.', button='OK')