import pygame, pywl, sys, os
from math import *

pygame.init()

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

size = (400, 400)
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption('Python Math Interpreter 2.0')
pygame.display.set_icon(pygame.image.load(resource_path(os.path.join('data', 'icon.png'))))

font = pygame.font.SysFont('malgungothic', 20)

black = (0, 0, 0)
darkBlue = (63, 63, 255)
blue = (127, 127, 255)
lightBlue = (191, 191, 255)
lightGray = (223, 223, 223)
white = (255, 255, 255)

ctrl = ['C', 'del', '=']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ops = ['+', '-', '*', '/', '%', '^']
mis = ['(', ')', '.', ',']
const = ['pi', 'e', 'phi']
funcs1 = ['abs', 'fact', 'sqrt', 'log', 'ln']
funcs2 = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']
funcs3 = ['csc', 'sec', 'cot', 'acsc', 'asec', 'acot']

def main():
    global size, screen
    
    rows = 9
    
    exp = pywl.Text(screen, '', font, black, (24, ((size[1] - 32) / rows - 8) / 2 + 16), 'west')

    control = [pywl.Button(screen, ctrl[i], font, black, (i * ((size[0] - 32) / len(ctrl)) + (i * 16 / len(ctrl)) + 16, 1 * ((size[1] - 32) / rows) + (1 * 16 / rows) + 16), ((size[0] - 32) / len(ctrl) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(ctrl))]
    numbers = [pywl.Button(screen, nums[i], font, black, (i * ((size[0] - 32) / len(nums)) + (i * 16 / len(nums)) + 16, 2 * ((size[1] - 32) / rows) + (2 * 16 / rows) + 16), ((size[0] - 32) / len(nums) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(nums))]
    operators = [pywl.Button(screen, ops[i], font, black, (i * ((size[0] - 32) / len(ops)) + (i * 16 / len(ops)) + 16, 3 * ((size[1] - 32) / rows) + (3 * 16 / rows) + 16), ((size[0] - 32) / len(ops) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(ops))]
    misc = [pywl.Button(screen, mis[i], font, black, (i * ((size[0] - 32) / len(mis)) + (i * 16 / len(mis)) + 16, 4 * ((size[1] - 32) / rows) + (4 * 16 / rows) + 16), ((size[0] - 32) / len(mis) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(mis))]
    constants = [pywl.Button(screen, const[i], font, black, (i * ((size[0] - 32) / len(const)) + (i * 16 / len(const)) + 16, 5 * ((size[1] - 32) / rows) + (5 * 16 / rows) + 16), ((size[0] - 32) / len(const) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(const))]
    functions1 = [pywl.Button(screen, funcs1[i], font, black, (i * ((size[0] - 32) / len(funcs1)) + (i * 16 / len(funcs1)) + 16, 6 * ((size[1] - 32) / rows) + (6 * 16 / rows) + 16), ((size[0] - 32) / len(funcs1) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(funcs1))]
    functions2 = [pywl.Button(screen, funcs2[i], font, black, (i * ((size[0] - 32) / len(funcs2)) + (i * 16 / len(funcs2)) + 16, 7 * ((size[1] - 32) / rows) + (7 * 16 / rows) + 16), ((size[0] - 32) / len(funcs2) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(funcs2))]
    functions3 = [pywl.Button(screen, funcs3[i], font, black, (i * ((size[0] - 32) / len(funcs3)) + (i * 16 / len(funcs3)) + 16, 8 * ((size[1] - 32) / rows) + (8 * 16 / rows) + 16), ((size[0] - 32) / len(funcs3) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(funcs3))]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                size = screen.get_size()

                exp.pos = (24, ((size[1] - 32) / rows - 8) / 2 + 16)

                control = [pywl.Button(screen, ctrl[i], font, black, (i * ((size[0] - 32) / len(ctrl)) + (i * 16 / len(ctrl)) + 16, 1 * ((size[1] - 32) / rows) + (1 * 16 / rows) + 16), ((size[0] - 32) / len(ctrl) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(ctrl))]
                numbers = [pywl.Button(screen, nums[i], font, black, (i * ((size[0] - 32) / len(nums)) + (i * 16 / len(nums)) + 16, 2 * ((size[1] - 32) / rows) + (2 * 16 / rows) + 16), ((size[0] - 32) / len(nums) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(nums))]
                operators = [pywl.Button(screen, ops[i], font, black, (i * ((size[0] - 32) / len(ops)) + (i * 16 / len(ops)) + 16, 3 * ((size[1] - 32) / rows) + (3 * 16 / rows) + 16), ((size[0] - 32) / len(ops) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(ops))]
                misc = [pywl.Button(screen, mis[i], font, black, (i * ((size[0] - 32) / len(mis)) + (i * 16 / len(mis)) + 16, 4 * ((size[1] - 32) / rows) + (4 * 16 / rows) + 16), ((size[0] - 32) / len(mis) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(mis))]
                constants = [pywl.Button(screen, const[i], font, black, (i * ((size[0] - 32) / len(const)) + (i * 16 / len(const)) + 16, 5 * ((size[1] - 32) / rows) + (5 * 16 / rows) + 16), ((size[0] - 32) / len(const) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(const))]
                functions1 = [pywl.Button(screen, funcs1[i], font, black, (i * ((size[0] - 32) / len(funcs1)) + (i * 16 / len(funcs1)) + 16, 6 * ((size[1] - 32) / rows) + (6 * 16 / rows) + 16), ((size[0] - 32) / len(funcs1) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(funcs1))]
                functions2 = [pywl.Button(screen, funcs2[i], font, black, (i * ((size[0] - 32) / len(funcs2)) + (i * 16 / len(funcs2)) + 16, 7 * ((size[1] - 32) / rows) + (7 * 16 / rows) + 16), ((size[0] - 32) / len(funcs2) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(funcs2))]
                functions3 = [pywl.Button(screen, funcs3[i], font, black, (i * ((size[0] - 32) / len(funcs3)) + (i * 16 / len(funcs3)) + 16, 8 * ((size[1] - 32) / rows) + (8 * 16 / rows) + 16), ((size[0] - 32) / len(funcs3) - 8, (size[1] - 32) / rows - 8), darkBlue, blue, lightBlue) for i in range(len(funcs3))]

        screen.fill(white)
        
        pygame.draw.rect(screen, darkBlue, (16, 16, size[0] - 32, (size[1] - 32) / rows - 8))
        pygame.draw.rect(screen, lightGray, (19, 19, size[0] - 38, (size[1] - 32) / rows - 14))

        exp.display()

        for i in control:
            i.display()

        for i in numbers:
            i.display()
            if i.value:
                if exp.text == 'error':
                    exp.text = ''
                if font.render(exp.text + i.text, True, black).get_rect()[2] <= size[0] - 48:
                    exp.text += i.text
        
        for i in operators:
            i.display()
            if i.value:
                if exp.text == 'error':
                    exp.text = ''
                if font.render(exp.text + i.text, True, black).get_rect()[2] <= size[0] - 48:
                    exp.text += i.text
        
        for i in misc:
            i.display()
            if i.value:
                if exp.text == 'error':
                    exp.text = ''
                if font.render(exp.text + i.text, True, black).get_rect()[2] <= size[0] - 48:
                    exp.text += i.text

        for i in constants:
            i.display()
            if i.value:
                if exp.text == 'error':
                    exp.text = ''
                if font.render(exp.text + i.text, True, black).get_rect()[2] <= size[0] - 48:
                    exp.text += i.text
        
        for i in functions1:
            i.display()
            if i.value:
                if exp.text == 'error':
                    exp.text = ''
                if font.render(exp.text + i.text + '(', True, black).get_rect()[2] <= size[0] - 48:
                    exp.text += i.text + '('

        for i in functions2:
            i.display()
            if i.value:
                if exp.text == 'error':
                    exp.text = ''
                if font.render(exp.text + i.text + '(', True, black).get_rect()[2] <= size[0] - 48:
                    exp.text += i.text + '('

        for i in functions3:
            i.display()
            if i.value:
                if exp.text == 'error':
                    exp.text = ''
                if font.render(exp.text + i.text + '(', True, black).get_rect()[2] <= size[0] - 48:
                    exp.text += i.text + '('

        pygame.display.flip()

        if control[0].value:
            exp.text = ''
        if control[1].value:
            exp.text = exp.text[:-1]
        if control[2].value and exp.text != '':
            try:
                exp.text = exp.text.replace('^', '**')
                exp.text = exp.text.replace('phi', '((sqrt(5)+1)/2)')
                exp.text = exp.text.replace('fact', 'factorial')
                exp.text = exp.text.replace('ln', 'log')
                exp.text = exp.text.replace('csc', '1/sin')
                exp.text = exp.text.replace('sec', '1/cos')
                exp.text = exp.text.replace('cot', '1/tan')
                exp.text = exp.text.replace('acsc', '1/asin')
                exp.text = exp.text.replace('asec', '1/acos')
                exp.text = exp.text.replace('acot', '1/atan')

                exp.text = str(eval(exp.text))
                
                if int(float(exp.text)) == float(exp.text):
                    exp.text = str(int(float(exp.text)))
            
            except:
                exp.text = 'error'

if __name__ == '__main__':
    main()
