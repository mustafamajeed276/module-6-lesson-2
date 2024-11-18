import pygame
def main():
    colors = {'red' : pygame.Color('red'),
              'green' : pygame.Color('green'),
              'blue' : pygame.Color('blue'),
              'yellow' : pygame.Color('yellow'),
              'white' : pygame.Color('white'),
              }
    current_color = colors['white']
    x, y = 30, 30
    spritewidth, spriteheight = 60, 60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] : x -= 3
        if pressed[pygame.K_RIGHT] : x += 3
        if pressed[pygame.K_DOWN] : y -= 3
        if pressed[pygame.K_UP] : y += 3
        x = min(max(0, x), screenwidth)