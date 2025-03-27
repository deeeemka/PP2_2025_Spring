import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

# Color constants
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Global game variables
SPEED = 5           
SCORE = 0           
COIN_SCORE = 0      

# Threshold to increase speed after collecting coins
COIN_SPEED_THRESHOLD = 5  
next_speed_increase_at = COIN_SPEED_THRESHOLD  # Next coin-score checkpoint

# Font setup
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load the background image
background = pygame.image.load("AnimatedStreet.png")

# Create a white display surface and set a title
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer Game")

#  ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the enemy image
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        # Start the enemy at a random x-position, off the top edge
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#  PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the player image
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        # Position the player near the bottom center
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

    def collect_coin(self, coins_group):
        collisions = pygame.sprite.spritecollide(self, coins_group, True)
        total_value = 0
        for coin in collisions:
            total_value += coin.value
        return total_value

#  COIN CLASS
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()

        # Random starting position (somewhere along top width)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        # Assign a random "value" or "weight" to each coin
        self.value = random.choice([1, 2, 3])

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            # Optionally re-randomize the coin's value each time it respawns:
            self.value = random.choice([1, 2, 3])

# SPRITE GROUPS
P1 = Player()                # The single Player
E1 = Enemy()                 # Initial Enemy
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()  

# This event increments speed every second
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# This event spawns new coins periodically (every 2 seconds, for example)
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 2000)

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Increment SPEED over time 
        if event.type == INC_SPEED:
            SPEED += 0.5

        # Spawn a new coin periodically
        if event.type == SPAWN_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # Fill the background
    DISPLAYSURF.blit(background, (0, 0))

    # Render scores
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)
    # Display enemy pass score (left) and coin score (right)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (SCREEN_WIDTH - 25, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check if Player collects any coins
    collected_value = P1.collect_coin(coins)
    if collected_value > 0:
        COIN_SCORE += collected_value
        # Check if we need to increase SPEED based on coin score
        if COIN_SCORE >= next_speed_increase_at:
            SPEED += 1
            next_speed_increase_at += COIN_SPEED_THRESHOLD

    # Check collision between Player and any Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        # Play crash sound
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        # Display Game Over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        # Remove all sprites and quit
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update display and tick
    pygame.display.update()
    FramePerSec.tick(FPS)