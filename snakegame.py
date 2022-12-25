import pygame
import random
import sys
# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Snake')

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the size of each block in the snake
block_size = 20

# Set the font style and size
font_style = pygame.font.SysFont("bahnschrift", 25)

# Set the score
score = 0

# Set the snake's starting position and movement direction
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the food position
food_pos = [random.randrange(1, (screen_width//block_size)) * block_size, random.randrange(1, (screen_height//block_size)) * block_size]
food_spawn = True

# Set the direction the snake is moving
direction = "RIGHT"
change_to = direction

# Set the clock
clock = pygame.time.Clock()

# Set the speed
speed = 15

# Create a function to display the score
def show_score(choice, color, font, size, x, y):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (x, y)
    else:
        score_rect.midtop = (x, y)
    screen.blit(score_surface, score_rect)

# Create a function to end the game
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Create a function to check if the snake has collided with the edges of the screen
def screen_collision(snake_head):
    if snake_head[0] >= screen_width or snake_head[0] < 0:
        game_over()
    if snake_head[1] >= screen_height or snake_head[1] < 0:
        game_over()

# Create a function to check if the snake has collided with itself
def self_collision(snake_body):
    if snake_body[0] in snake_body[1:]:
        game_over()

# Create a function to check if the snake has eaten the food
def food_collision(snake_pos, food_pos):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    else:
        return False

# Create a function to generate new food
def spawn_food():
    food_pos = [random.randrange(1, (screen_width//block_size)) * block_size, random.randrange(1, (screen_height//block_size)) * block_size]
    return food_pos

# Create a function to move the snake
def snake_movement():
    if change_to == 'UP':
        snake_pos[1] -= block_size
    if change_to == 'DOWN':
        snake_pos[1] += block_size
    if change_to == 'LEFT':
        snake_pos[0] -= block_size
    if change_to == 'RIGHT':
        snake_pos[0] += block_size

# Create a function to display the snake
def snake(block_size, snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], block_size, block_size))

# Create the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Check if the snake has collided with the edges of the screen
    screen_collision(snake_pos)

    # Check if the snake has collided with itself
    self_collision(snake_body)

    # Check if the snake has eaten the food
    if food_collision(snake_pos, food_pos):
        food_spawn = False
        score += 1
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = spawn_food()
        food_spawn = True

    # Update the snake's position
    snake_movement()
    snake_body.insert(0, list(snake_pos))

    # Clear the screen
    screen.fill(black)

    # Draw the snake and food
    snake(block_size, snake_body)
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))


    # Display the score
    show_score(1, white, "consolas", 20, screen_width/10, 15)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(speed)

