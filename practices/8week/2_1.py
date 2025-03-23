import pygame
import random

#Pygame Initialization
pygame.init()

#Window and grid sizes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

#Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)

#Directions of movement of the snake
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.alive = True  #Flag to check if the snake is alive

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        if not self.alive:
            return
        
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)

        #Wall Collision Check
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            self.alive = False
            return

        #Self-collision check
        if new_head in self.positions:
            self.alive = False
            return

        #Moving of the snake
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.__init__()  #Restart snake

    def draw(self, surface):
        for segment in self.positions:
            pygame.draw.rect(surface, self.color, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, WHITE, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE), 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

#Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position([])

    #Generate food in a random position, excluding the snake
    def randomize_position(self, snake_positions):
        while True:
            new_position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
            if new_position not in snake_positions:
                self.position = new_position
                break
    
    #Drawing food on the screen
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, WHITE, pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE), 1)

#The function of drawing text on the screen
def draw_text(surface, text, x, y, size=36, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

#Screen of death with the ability to restart
def game_over_screen(score):
    screen.fill(DARK_BLUE)
    draw_text(screen, "You DIED", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 50, WHITE)
    draw_text(screen, f"YOUR SCORE: {score}", SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 40, WHITE)
    draw_text(screen, "     Press SPACE to restart or ESC to exit", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 50, 30, WHITE)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  #Restart
                    return
                elif event.key == pygame.K_ESCAPE:  #Exit
                    pygame.quit()
                    exit()

#Main function of the game
def main():
    while True:
        snake = Snake()
        food = Food()
        score = 0
        level = 1
        clock = pygame.time.Clock()

        while snake.alive:
            screen.fill(BLACK)  #Cleaning the screen 
            snake.handle_keys()
            snake.move()

            #Food Eating Test
            if snake.get_head_position() == food.position:
                snake.length += 1
                score += 1
                food.randomize_position(snake.positions)

                #Level up every 3 points
                if score % 3 == 0:
                    level += 1

            #Death check
            if not snake.alive:
                game_over_screen(score)
                break  #Exiting the game loop and restarting

            #Rendering objects
            snake.draw(screen)
            food.draw(screen)

            #Display score and level
            draw_text(screen, f"Score: {score}", 10, 10)
            draw_text(screen, f"Level: {level}", 10, 40)

            pygame.display.update()
            clock.tick(8 + level)  #Increase snake speed as you level up

if __name__ == '__main__':
    main()