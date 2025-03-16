import pygame

pygame.init() 

WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((800, 480)) 

COLOR_RED = (255, 0, 0) 
COLOR_BLUE = (0, 0, 255)

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

pos = 20

running = True

clock = pygame.time.Clock()
FPS = 60 

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()       
    if pressed_keys[pygame.K_UP] and circle_y - 20>0:
        circle_y -= pos
    if pressed_keys[pygame.K_DOWN] and circle_y +20<HEIGHT:
        circle_y += pos
    if pressed_keys[pygame.K_LEFT] and circle_x - 20>0:
        circle_x -= pos
    if pressed_keys[pygame.K_RIGHT] and circle_x +20<WIDTH:
        circle_x += pos
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 25)
    
    pygame.display.flip() 
    clock.tick(FPS) 