import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800 , 600))
running = True
bg_image = pygame.image.load('clock.png')
sec_image = pygame.image.load('sec_hand.png')
min_image = pygame.image.load('min_hand.png')
rect = bg_image.get_rect(center=(400,300))
clock = pygame.time.Clock()
FPS = 60

while running:
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time = datetime.now().time()

    sec_angle = -(time.second * 6)
    sec_img = pygame.transform.rotate(sec_image , sec_angle)
    sec_rect = sec_img.get_rect(center=rect.center)
    screen.blit(sec_img, sec_rect.topleft)

    min_angle = -(time.minute * 6)
    min_img = pygame.transform.rotate(min_image , min_angle)
    min_rect = min_img.get_rect(center=rect.center)
    screen.blit(min_img, min_rect.topleft)

    pygame.display.flip()
    clock.tick(FPS)