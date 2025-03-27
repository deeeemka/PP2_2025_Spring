import pygame
import random
import sys

#   Pygame Initialization
pygame.init()

#   Window and Grid Parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
WHITE     = (255, 255, 255)
GREEN     = (0, 255, 0)
RED       = (255, 0, 0)
BLACK     = (0, 0, 0)
DARK_BLUE = (0, 0, 100)

# Movement Directions
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

# SNAKE CLASS
class Snake:
    """
    The Snake class holds:
      - Positions of its body segments
      - Current movement direction
      - A flag to check if it's alive
      - Methods to move, draw, and handle key presses
    """
    def __init__(self):
        self.length = 1
        # Start snake in the center of the screen
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.alive = True  # Flag to check if the snake is alive

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        if not self.alive:
            return
        
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        # New head position based on direction
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)

        # Check wall collisions
        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
            self.alive = False
            return

        # Check self-collision
        if new_head in self.positions:
            self.alive = False
            return

        # Insert the new head and remove the tail if needed
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.__init__()

    def draw(self, surface):
        for segment in self.positions:
            pygame.draw.rect(surface, self.color,
                             pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, WHITE,
                             pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE), 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

# FOOD CLASS
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        # Each piece of food will have a random "weight" or "value"
        self.value = 1
        # Track when the food was last spawned
        self.spawn_time = pygame.time.get_ticks()
        # Time (in milliseconds) after which food disappears if not eaten
        self.disappear_time = 5000  # 5 seconds
        # Randomize position and value
        self.randomize_position([])

    def randomize_position(self, snake_positions):
        while True:
            new_position = (
                random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            )
            if new_position not in snake_positions:
                self.position = new_position
                break
        
        # Randomize food's weight/value from 1 to 3 (adjust as desired)
        self.value = random.randint(1, 3)
        # Reset the spawn time each time the food is placed
        self.spawn_time = pygame.time.get_ticks()

    def update(self, snake_positions):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > self.disappear_time:
            # Food has expired; move it somewhere else
            self.randomize_position(snake_positions)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, WHITE,
                         pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE), 1)

#  UTILITY FUNCTION: DRAW TEXT
def draw_text(surface, text, x, y, size=36, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# GAME OVER SCREEN
def game_over_screen(score):
    screen.fill(DARK_BLUE)
    draw_text(screen, "You DIED", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 50, WHITE)
    draw_text(screen, f"YOUR SCORE: {score}", SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 40, WHITE)
    draw_text(screen, "     Press SPACE to restart or ESC to exit",
              SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 50, 30, WHITE)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Restart
                    return
                elif event.key == pygame.K_ESCAPE:  # Exit
                    pygame.quit()
                    sys.exit()

# MAIN GAME FUNCTION
def main():
    while True:
        snake = Snake()
        food = Food()
        score = 0
        level = 1
        clock = pygame.time.Clock()

        # While the snake is alive, keep running the game loop
        while snake.alive:
            screen.fill(BLACK)  # Clear the screen each frame
            snake.handle_keys()
            snake.move()

            # Check if the snake ate the food
            if snake.get_head_position() == food.position:
                snake.length += 1
                score += food.value
                food.randomize_position(snake.positions)

                # Increase level every 3 points (you can change this logic)
                if score % 3 == 0:
                    level += 1

            # Check if the snake has died (via self-collision or wall)
            if not snake.alive:
                game_over_screen(score)
                break

            # Update the food (check if it has expired)
            food.update(snake.positions)

            # Render objects on the screen
            snake.draw(screen)
            food.draw(screen)

            # Display score and level
            draw_text(screen, f"Score: {score}", 10, 10)
            draw_text(screen, f"Level: {level}", 10, 40)
            draw_text(screen, f"Food Value: {food.value}", 10, 70)

            pygame.display.update()

            # Increase snake speed based on level
            clock.tick(8 + level)

if __name__ == '__main__':
    main()
