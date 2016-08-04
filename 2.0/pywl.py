import pygame
import sys

pygame.init()

xsmallfont = pygame.font.SysFont("consolas", 18)

black = (0, 0, 0)
white = (255, 255, 255)

class Text:
    def __init__(self, screen, text, font, color, pos, textpos = "center"):
        self.screen = screen
        self.text = text
        self.font = font
        self.color = color
        self.pos = pos
        self.textpos = textpos

    def display(self):
        textSurf = self.font.render(self.text, True, self.color)
        textRect = textSurf.get_rect()
        
        if self.textpos == "center":
            textRect.center = self.pos[0], self.pos[1]
        elif self.textpos == "north":
            textRect.midtop = self.pos[0], self.pos[1]
        elif self.textpos == "northeast":
            textRect.topright = self.pos[0], self.pos[1]
        elif self.textpos == "east":
            textRect.midright = self.pos[0], self.pos[1]
        elif self.textpos == "southeast":
            textRect.bottomright = self.pos[0], self.pos[1]
        elif self.textpos == "south":
            textRect.midbottom = self.pos[0], self.pos[1]
        elif self.textpos == "southwest":
            textRect.bottomleft = self.pos[0], self.pos[1]
        elif self.textpos == "west":
            textRect.midleft = self.pos[0], self.pos[1]
        elif self.textpos == "northwest":
            textRect.topleft = self.pos[0], self.pos[1]
        
        self.screen.blit(textSurf, textRect)

class Checkbox:
    def __init__(self, screen, default, pos, size, inactive, active, activated, clickable = True):
        self.screen = screen
        self.value = default
        self.pos = pos
        self.size = size
        self.inactive = inactive
        self.active = active
        self.activated = activated
        self.clickable = clickable
        self.clicking = False

    def display(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        pygame.draw.rect(self.screen, black, (self.pos[0], self.pos[1], self.size, self.size))

        if self.pos[0] <= cur[0] <= self.pos[0] + self.size and self.pos[1] <= cur[1] <= self.pos[1] + self.size and self.clickable:
            if click:
                pygame.draw.rect(self.screen, self.activated, (self.pos[0] + 3, self.pos[1] + 3, self.size - 6, self.size - 6))
            else:
                pygame.draw.rect(self.screen, self.active, (self.pos[0] + 3, self.pos[1] + 3, self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(self.screen, self.inactive, (self.pos[0] + 3, self.pos[1] + 3, self.size - 6, self.size - 6))

        if self.value:
            pygame.draw.line(self.screen, black, (self.pos[0] + 6, self.pos[1] + self.size / 2), (self.pos[0] + self.size / 2, self.pos[1] + self.size - 6), 3)
            pygame.draw.line(self.screen, black, (self.pos[0] + self.size / 2, self.pos[1] + self.size - 6), (self.pos[0] + self.size - 6, self.pos[1] + 6), 3)
        
        if self.pos[0] <= cur[0] <= self.pos[0] + self.size and self.pos[1] <= cur[1] <= self.pos[1] + self.size and self.clickable and self.clicking and not click:
            self.value = not self.value
            self.clicking = False
        
        self.clicking = click

class Button:
    def __init__(self, screen, text, font, color, pos, size, inactive, active, activated, clickable = True):
        self.screen = screen
        self.text = text
        self.font = font
        self.color = color
        self.pos = pos
        self.size = size
        self.inactive = inactive
        self.active = active
        self.activated = activated
        self.clickable = clickable
        self.clicking = False
        self.value = False

    def display(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        
        self.value = False
        
        pygame.draw.rect(self.screen, black, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        
        if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] <= cur[1] <= self.pos[1] + self.size[1] and self.clickable:
            if click:
                pygame.draw.rect(self.screen, self.activated, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))
            else:
                pygame.draw.rect(self.screen, self.active, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))
        else:
            pygame.draw.rect(self.screen, self.inactive, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))

        Text(self.screen, self.text, self.font, self.color, (self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2)).display()

        if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] <= cur[1] <= self.pos[1] + self.size[1] and self.clickable and self.clicking and not click:
            self.value = True

        self.clicking = click

class Slider:
    def __init__(self, screen, default, pos, interval, size, inactive, active, activated, clickable = True):
        self.screen = screen
        self.value = default
        self.pos = pos
        self.interval = interval
        self.size = size
        self.inactive = inactive
        self.active = active
        self.activated = activated
        self.clickable = clickable
        self.clicking = False
    
    def display(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        pygame.draw.line(self.screen, black, (self.pos[0] + self.size / 2, self.pos[1] + self.size), (self.pos[0] + self.interval[1] - self.interval[0] + self.size / 2, self.pos[1] + self.size), self.size / 10)
        pygame.draw.rect(self.screen, black, (self.pos[0] + self.value - self.interval[0], self.pos[1], self.size, self.size))

        if self.pos[0] + self.value - self.interval[0] <= cur[0] <= self.pos[0] + self.value - self.interval[0] + self.size and self.pos[1] <= cur[1] <= self.pos[1] + self.size and self.clickable:
            if click:
                pygame.draw.rect(self.screen, self.activated, (self.pos[0] + self.value - self.interval[0] + 3, self.pos[1] + 3, self.size - 6, self.size - 6))
                self.clicking = True
            else:
                pygame.draw.rect(self.screen, self.active, (self.pos[0] + self.value - self.interval[0] + 3, self.pos[1] + 3, self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(self.screen, self.inactive, (self.pos[0] + self.value - self.interval[0] + 3, self.pos[1] + 3, self.size - 6, self.size - 6))

        if self.clicking:
            self.value = cur[0] - self.pos[0] + self.interval[0] - self.size / 2
            if self.value < self.interval[0]:
                self.value = self.interval[0]
            elif self.value > self.interval[1]:
                self.value = self.interval[1]

        if not click:
            self.clicking = False

class Dropdown:
    def __init__(self, screen, options, selected, font, color, pos, size, inactive, active, activated, clickable = True):
        self.screen = screen
        self.options = options
        self.value = selected
        self.font = font
        self.color = color
        self.pos = pos
        self.size = size
        self.inactive = inactive
        self.active = active
        self.activated = activated
        self.clickable = clickable
        self.clicking = False
        self.open = False

    def display(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        pygame.draw.rect(self.screen, black, (self.pos[0], self.pos[1], self.size[0], self.size[1]))

        if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] <= cur[1] <= self.pos[1] + self.size[1] - 4 and self.clickable:
            if click:
                pygame.draw.rect(self.screen, self.activated, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))
            else:
                pygame.draw.rect(self.screen, self.active, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))
        else:
            pygame.draw.rect(self.screen, self.inactive, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))

        Text(self.screen, self.options[self.value], self.font, self.color, (self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2)).display()

        if self.open:
            total = 1
            
            for i in range(len(self.options)):
                if i != self.value:
                    pygame.draw.rect(self.screen, black, (self.pos[0], self.pos[1] + (self.size[1] - 3) * total, self.size[0], self.size[1]))
                    
                    if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] + (self.size[1] - 3) * total <= cur[1] <= self.pos[1] + (self.size[1] - 3) * (total + 1) - 1 and self.clickable:
                        if click:
                            pygame.draw.rect(self.screen, self.activated, (self.pos[0] + 3, self.pos[1] + 3 + (self.size[1] - 3) * total, self.size[0] - 6, self.size[1] - 6))
                        else:
                            pygame.draw.rect(self.screen, self.active, (self.pos[0] + 3, self.pos[1] + 3 + (self.size[1] - 3) * total, self.size[0] - 6, self.size[1] - 6))
                    else:
                        pygame.draw.rect(self.screen, self.inactive, (self.pos[0] + 3, self.pos[1] + 3 + (self.size[1] - 3) * total, self.size[0] - 6, self.size[1] - 6))

                    Text(self.screen, self.options[i], self.font, self.color, (self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2 + (self.size[1] - 3) * total)).display()

                    if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] + (self.size[1] - 3) * total <= cur[1] <= self.pos[1] + (self.size[1] - 3) * (total + 1) - 1 and self.clickable and self.clicking and not click:
                        self.value = i
                        self.open = False

                    total += 1

        if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] <= cur[1] <= self.pos[1] + self.size[1] and self.clickable and self.clicking and not click:
            self.open = not self.open
        elif self.clicking and not click:
            self.open = False

        self.clicking = click

class Input:
    def __init__(self, screen, default, font, color, pos, size, limit, inactive, active, activated, clickable = True):
        self.screen = screen
        self.value = default
        self.font = font
        self.color = color
        self.pos = pos
        self.size = size
        self.limit = limit
        self.inactive = inactive
        self.active = active
        self.activated = activated
        self.clickable = clickable
        self.clicking = False
        self.open = False
        self.pressing = []

    def display(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        
        keys = pygame.key.get_pressed()

        textpos = self.font.render(self.value, True, self.color).get_rect()

        pygame.draw.rect(self.screen, black, (self.pos[0], self.pos[1], self.size[0], self.size[1]))

        if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] <= cur[1] <= self.pos[1] + self.size[1] and self.clickable:
            if click:
                pygame.draw.rect(self.screen, self.activated, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))
            else:
                pygame.draw.rect(self.screen, self.active, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))
        else:
            pygame.draw.rect(self.screen, self.inactive, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))

        if self.open:
            pygame.draw.rect(self.screen, self.activated, (self.pos[0] + 3, self.pos[1] + 3, self.size[0] - 6, self.size[1] - 6))

            if keys[pygame.K_BACKSPACE] and pygame.K_BACKSPACE not in self.pressing:
                self.value = self.value[:-1]
            elif keys[pygame.K_RETURN]:
                self.open = False
            else:
                for i in range(128):
                    if keys[i] and i not in self.pressing and len(self.value) < self.limit and textpos[2] < self.size[0] - 20:
                        if not keys[pygame.K_LSHIFT] and not keys[pygame.K_RSHIFT]:
                            self.value += chr(i)
                        else:
                            shift = [39, 34, 44, 60, 45, 95, 46, 62, 47, 63, 48, 41, 49, 33, 50, 64, 51, 35, 52, 36, 53, 37, 54, 94, 55, 38, 56, 42, 57, 40, 59, 58, 61, 43, 91, 123, 92, 124, 93, 125, 96, 126]
                            for j in range(0, len(shift) - 1, 2):
                                if i == shift[j] and shift[j + 1]:
                                    self.value += chr(shift[j + 1])
                            if 97 <= i <= 122:
                                self.value += chr(i - 32)

        Text(self.screen, self.value, self.font, self.color, (self.pos[0] + 10, self.pos[1] + self.size[1] / 2), "west").display()

        if self.pos[0] <= cur[0] <= self.pos[0] + self.size[0] and self.pos[1] <= cur[1] <= self.pos[1] + self.size[1] and self.clickable and self.clicking and not click:
            self.open = True
        elif self.clicking and not click:
            self.open = False

        self.clicking = click

        self.pressing = []
        for k in range(128):
            if keys[k]:
                self.pressing.append(k)

if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("PyWL")

    text = Text(screen, "Text", xsmallfont, (0, 191, 0), (400, 50))
    check = Checkbox(screen, True, (100, 100), 30, (63, 63, 255), (127, 127, 255), (191, 191, 255))
    button = Button(screen, "button", xsmallfont, black, (200, 100), (100, 50), (191, 0, 0), (255, 0, 0), (255, 63, 63))
    slider = Slider(screen, 135, (400, 100), (1, 270), 30, (191, 191, 0), (255, 255, 0), (255, 255, 63))
    dropdown = Dropdown(screen, ["one", "two", "three", "four"], 0, xsmallfont, black, (200, 200), (100, 50), (191, 0, 191), (255, 0, 255), (255, 63, 255))
    entry = Input(screen, "string input", xsmallfont, black, (400, 200), (300, 50), 50, (0, 191, 0), (0, 255, 0), (127, 255, 127))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)

        text.display()
        check.display()
        button.display()
        slider.display()
        dropdown.display()
        entry.display()
        
        pygame.display.flip()
