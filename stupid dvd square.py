import sys
import math
import random
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (640, 480)
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption('absolute garbage')

# Create the square
square_size = 50
square = pygame.Rect(0, 0, square_size, square_size)

# Set the initial position and velocity of the square
square_x = window_size[0] // 2
square_y = window_size[1] // 2
velocity = [0.15, 0.15]

# Set up the buttons
increase_button_size = (100, 50)
increase_button_pos = (25, 50)
increase_button = pygame.Rect(increase_button_pos, increase_button_size)

decrease_button_size = (100, 50)
decrease_button_pos = (150, 50)
decrease_button = pygame.Rect(decrease_button_pos, decrease_button_size)

# Set the initial color of the square
color = (255, 255, 255)

# Create clock object
clock = pygame.time.Clock()

# Set up the font for displaying the velocity
font = pygame.font.Font(None, 32)

# Set the velocity limit
velocity_limit = 12

# Run the game loop
while True:
    # Update the position of the square
    square_x += velocity[0]
    square_y += velocity[1]
    square.x = int(square_x)
    square.y = int(square_y)

    
    # Check for collisions with the edges of the window
    if square.left < 0 or square.right > window_size[0]:
        velocity[0] = -velocity[0]
        # Change the color of the square to a random color
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if square.top < 0 or square.bottom > window_size[1]:
        velocity[1] = -velocity[1]
        # Change the color of the square to a random color
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Check the position of the mouse
    mouse_pos = pygame.mouse.get_pos()
    
    # Change the cursor based on the position of the mouse
    if increase_button.collidepoint(mouse_pos) or decrease_button.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    # Draw the square and buttons to the window
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, square)
    pygame.draw.rect(screen, (0, 255, 0), increase_button)
    pygame.draw.rect(screen, (255, 0, 0), decrease_button)
    
    # Create a surface with the velocity text drawn on it
    velocity_text = font.render(f"Velocity: {velocity}", True, (255, 255, 255))
    
    # Blit the text surface onto the screen
    screen.blit(velocity_text, (25, 110))
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        # Check for window resize events
        elif event.type == VIDEORESIZE:
            window_size = event.size
            screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
            # Redraw the screen with the new window size
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), square)
            pygame.draw.rect(screen, (0, 255, 0), increase_button)
            pygame.draw.rect(screen, (255, 0, 0), decrease_button)
            pygame.display.update()

        # Check for mouse clicks on the buttons
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_buttons = pygame.mouse.get_pressed()
            
            if increase_button.collidepoint(mouse_pos) and mouse_buttons[0]:
                # Increase the velocity of the square
                velocity[0] *= 1.2
                velocity[1] *= 1.2
            elif decrease_button.collidepoint(mouse_pos) and mouse_buttons[0]:
                # Decrease the velocity of the square
                velocity[0] *= 0.8
                velocity[1] *= 0.8

        # Check if the velocity exceeds the limit
        velocity_magnitude = math.hypot(velocity[0], velocity[1])
        if velocity_magnitude > velocity_limit:
            # Scale the velocity down to the limit
            velocity[0] *= velocity_limit / velocity_magnitude
            velocity[1] *= velocity_limit / velocity_magnitude
    
    # Limit the framerate to 60 fps
    clock.tick(60)



