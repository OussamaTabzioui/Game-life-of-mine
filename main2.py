import pygame
import sys
from settings import *

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Football Match Simulation")

# Define some constants
BALL_RADIUS = 10
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 60
TEAM_COLOR_1 = (0, 0, 255)  # Blue
TEAM_COLOR_2 = (255, 0, 0)  # Red
SPEED_INCREMENT = 0.1
MAX_BALL_SPEED = 10

# Define initial positions
ball_pos = [width // 2, height // 2]
ball_vel = [2, 2]

player1_pos = [50, height // 2 - PLAYER_HEIGHT // 2]
player2_pos = [width - 5 - PLAYER_WIDTH, height // 2 - PLAYER_HEIGHT // 2]

# Set up player movement speed
player_speed = 7
player1_move_up = False
player1_move_down = False
player2_move_up = False
player2_move_down = False

# Set up ball speed increment
ball_speed_increment_timer = 0
speed_increment_interval = 1000  # Time in milliseconds

# Main game loop
while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_move_up = True
            if event.key == pygame.K_DOWN:
                player1_move_down = True
            if event.key == pygame.K_w:
                player2_move_up = True
            if event.key == pygame.K_s:
                player2_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_move_up = False
            if event.key == pygame.K_DOWN:
                player1_move_down = False
            if event.key == pygame.K_w:
                player2_move_up = False
            if event.key == pygame.K_s:
                player2_move_down = False

    # Move the ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball collision with top and bottom walls
    if ball_pos[1] - BALL_RADIUS < 0 or ball_pos[1] + BALL_RADIUS > height:
        ball_vel[1] = -ball_vel[1]

    # Ball collision with players
    if (player1_pos[0] < ball_pos[0] < player1_pos[0] + PLAYER_WIDTH and
        player1_pos[1] < ball_pos[1] < player1_pos[1] + PLAYER_HEIGHT) or \
       (player2_pos[0] < ball_pos[0] < player2_pos[0] + PLAYER_WIDTH and
        player2_pos[1] < ball_pos[1] < player2_pos[1] + PLAYER_HEIGHT):
        ball_vel[0] = -ball_vel[0]

    # Ball out of bounds
    if ball_pos[0] - BALL_RADIUS < 0 or ball_pos[0] + BALL_RADIUS > width:
        ball_pos = [width // 2, height // 2]
        ball_vel = [2, 2]

    # Player movement
    if player1_move_up and player1_pos[1] > 0:
        player1_pos[1] -= player_speed
    if player1_move_down and player1_pos[1] < height - PLAYER_HEIGHT:
        player1_pos[1] += player_speed
    if player2_move_up and player2_pos[1] > 0:
        player2_pos[1] -= player_speed
    if player2_move_down and player2_pos[1] < height - PLAYER_HEIGHT:
        player2_pos[1] += player_speed

    # Increase ball speed over time
    if current_time - ball_speed_increment_timer > speed_increment_interval:
        ball_speed_increment_timer = current_time
        # Increase speed, ensuring it does not exceed MAX_BALL_SPEED
        ball_vel[0] = min(MAX_BALL_SPEED, ball_vel[0] * (1 + SPEED_INCREMENT))
        ball_vel[1] = min(MAX_BALL_SPEED, ball_vel[1] * (1 + SPEED_INCREMENT))

    # Draw the game state
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)
    pygame.draw.rect(screen, TEAM_COLOR_1, (player1_pos[0], player1_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, TEAM_COLOR_2, (player2_pos[0], player2_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT))

    # Update the display
    pygame.display.flip()




    # Cap the frame rate
    pygame.time.Clock().tick(60)
