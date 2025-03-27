import pygame
import math
import sys

# Pygame Initialization
pygame.init()

# Screen Parameters
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Painter")

# Colors
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
PURPLE = (128, 0, 128)

# Fill the background with white
screen.fill(WHITE)

#  Color Selection Buttons
COLOR_BUTTONS = [
    {"color": RED,    "rect": pygame.Rect(10,  10, 50, 50)},
    {"color": YELLOW, "rect": pygame.Rect(70,  10, 50, 50)},
    {"color": GREEN,  "rect": pygame.Rect(130, 10, 50, 50)},
    {"color": BLUE,   "rect": pygame.Rect(190, 10, 50, 50)},
    {"color": PURPLE, "rect": pygame.Rect(250, 10, 50, 50)}
]

# Load eraser image
eraser_img = pygame.image.load('eraser.png')
eraser_img = pygame.transform.scale(eraser_img, (50, 50))

#    Tool Selection Buttons
TOOLS = [
    {"name": "Pencil",   "rect": pygame.Rect(320, 10, 60, 40), "type": "pencil"},
    {"name": "Rect",     "rect": pygame.Rect(385, 10, 60, 40), "type": "rectangle"},
    {"name": "Circle",   "rect": pygame.Rect(450, 10, 60, 40), "type": "circle"},
    {"name": "Square",   "rect": pygame.Rect(515, 10, 60, 40), "type": "square"},
    {"name": "R.Tri",    "rect": pygame.Rect(580, 10, 60, 40), "type": "right_triangle"},
    {"name": "E.Tri",    "rect": pygame.Rect(645, 10, 60, 40), "type": "equilateral_triangle"},
    {"name": "Rhombus",  "rect": pygame.Rect(710, 10, 80, 40), "type": "rhombus"},
]

# Eraser selection button (near the right edge)
eraser_button = pygame.Rect(830, 10, 50, 50)

# Current Tool Settings
current_color = RED       
current_tool  = "pencil"  
drawing       = False     
start_pos     = None      
last_pos      = None      

#     Drawing Functions
def draw_pencil(surface, color, start, end, width=3):
    pygame.draw.line(surface, color, start, end, width)

def draw_rectangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    left = min(x1, x2)
    top  = min(y1, y2)
    pygame.draw.rect(surface, color, (left, top, w, h), 3)

def draw_circle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    radius = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    pygame.draw.circle(surface, color, start, radius, 3)

def draw_square(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    width  = abs(x2 - x1)
    height = abs(y2 - y1)
    side   = min(width, height)  # side length is the smaller of width or height

    left = min(x1, x2)
    top  = min(y1, y2)
    pygame.draw.rect(surface, color, (left, top, side, side), 3)

def draw_right_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    left   = min(x1, x2)
    right  = max(x1, x2)
    top    = min(y1, y2)
    bottom = max(y1, y2)
    
    # Points for a right triangle
    points = [(left, top), (right, top), (left, bottom)]
    pygame.draw.polygon(surface, color, points, 3)

def draw_equilateral_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    left   = min(x1, x2)
    right  = max(x1, x2)
    top    = min(y1, y2)
    bottom = max(y1, y2)

    width  = right - left
    height = bottom - top
    side   = min(width, height)

    eq_height = side * (math.sqrt(3) / 2)

    xA = left
    yA = top + side
    xB = left + side
    yB = top + side
    # Top vertex (centered horizontally)
    xC = left + side / 2
    yC = (top + side) - eq_height

    # Draw the triangle
    points = [(xA, yA), (xB, yB), (xC, yC)]
    pygame.draw.polygon(surface, color, points, 3)

def draw_rhombus(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    left   = min(x1, x2)
    right  = max(x1, x2)
    top    = min(y1, y2)
    bottom = max(y1, y2)

    cx = (left + right) / 2  
    cy = (top + bottom) / 2  

    # Diamond corners (top, right, bottom, left)
    points = [
        (cx,   top),    
        (right, cy),    
        (cx,   bottom), 
        (left,  cy)     
    ]
    pygame.draw.polygon(surface, color, points, 3)

def erase_area(surface, position):
    pygame.draw.circle(surface, WHITE, position, 20)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        # Mouse button down (click)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                for button in TOOLS:
                    if button["rect"].collidepoint(event.pos):
                        current_tool = button["type"]

                if eraser_button.collidepoint(event.pos):
                    current_tool = "eraser"

                for button in COLOR_BUTTONS:
                    if button["rect"].collidepoint(event.pos):
                        current_color = button["color"]

                start_pos = event.pos
                last_pos  = event.pos
                drawing   = True

        # Mouse button up (release)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  
                drawing = False
                end_pos = event.pos

                if start_pos and end_pos:
                    if current_tool == "rectangle":
                        draw_rectangle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "circle":
                        draw_circle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "square":
                        draw_square(screen, current_color, start_pos, end_pos)
                    elif current_tool == "right_triangle":
                        draw_right_triangle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "equilateral_triangle":
                        draw_equilateral_triangle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "rhombus":
                        draw_rhombus(screen, current_color, start_pos, end_pos)

        # Mouse movement
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == "pencil":
                    draw_pencil(screen, current_color, last_pos, event.pos, 3)
                    last_pos = event.pos
                elif current_tool == "eraser":
                    erase_area(screen, event.pos)

    # Draw color buttons
    for button in COLOR_BUTTONS:
        pygame.draw.rect(screen, button["color"], button["rect"])

    # Draw shape/tool buttons
    for button in TOOLS:
        pygame.draw.rect(screen, BLACK, button["rect"], 2)
        font = pygame.font.Font(None, 24)
        text = font.render(button["name"], True, BLACK)
        screen.blit(text, (button["rect"].x + 5, button["rect"].y + 10))

    # Draw eraser button
    pygame.draw.rect(screen, BLACK, eraser_button, 2)
    screen.blit(eraser_img, (eraser_button.x, eraser_button.y))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
