
import pygame
import math
import time

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 800

# Set the window title
pygame.display.set_caption("Circles")

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the radius of the larger circle
radius = 200

# Set the radius of the smaller circle
small_radius = radius / 2

# Set the rotation speed of the smaller circle, in revolutions per second
rotation_speed = 1

# Set the color of the circle and stick
color = (0, 255, 0) # Green

# Set the length of the stick
stick_length = small_radius

# Set the starting angle of the smaller circle
angle = 0

# Set the rotation speed of the stick, in revolutions per second
stick_rotation_speed = 2

# Set previous stick end position
prev_mouse_x = screen_width  / 2 + radius
prev_mouse_y = screen_height / 2

Showsmallcircle = 1
Showstick = 1

# Run the game loop
running = True
while running:
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_r]:
        screen.fill((0, 0, 0))
    if pressed[pygame.K_w]:
        stick_rotation_speed +=0.1
    if pressed[pygame.K_s]:
        stick_rotation_speed -=0.1
    if pressed[pygame.K_q]:
        rotation_speed +=0.1
    if pressed[pygame.K_a]:
        rotation_speed -=0.1
    if pressed[pygame.K_z]:
        Showsmallcircle = 0
    if pressed[pygame.K_x]:
        Showsmallcircle = 1
    if pressed[pygame.K_c]:
        Showstick = 0
    if pressed[pygame.K_v]:
        Showstick = 1
    
    # Calculate the x and y position of the smaller circle based on the angle
    x = radius / 2 * math.cos(angle) + screen_width / 2
    y = radius / 2 * math.sin(angle) + screen_height / 2

    # Calculate the x and y positions of the endpoints of the stick
    stick_x1 = x
    stick_y1 = y
    stick_x2 = x + stick_length * math.cos(angle * stick_rotation_speed)
    stick_y2 = y + stick_length * math.sin(angle * stick_rotation_speed)

    # Get the stick end position
    mouse_x, mouse_y = stick_x2, stick_y2

    # Draw a white line from the previous stick end position to the current stick end position
    pygame.draw.line(screen, (255, 255, 255), (prev_mouse_x, prev_mouse_y), (mouse_x, mouse_y), 2)

    # Store the current stick end position for the next iteration
    prev_mouse_x = mouse_x
    prev_mouse_y = mouse_y
    
    # Draw the larger circle outline
    pygame.draw.circle(screen, color, (screen_width // 2, screen_height // 2), radius, 1)

    # Draw the smaller circle outline
    if Showsmallcircle == 1:
        pygame.draw.circle(screen, color, (int(x), int(y)), small_radius, 1)

    # Draw the stick
    if Showstick == 1:
        pygame.draw.line(screen, color, (stick_x1, stick_y1), (stick_x2, stick_y2), 1)

    # Update the angle of the smaller circle
    angle += rotation_speed * 2 * math.pi / 60

    # Update the screen
    pygame.display.flip()

    # Wait for one frame
    time.sleep(1/60)
    
# Quit Pygame
pygame.quit()
