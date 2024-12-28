import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRAVITY = 0.25
BIRD_SPEED = 5
BIRD_JUMP = -5
PIPE_WIDTH = 50
PIPE_HEIGHT = random.randint(100, 150)
PIPE_GAP = 150
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("C:\\Users\\YUSUF\\Desktop\\Docs\\KE\\jpeg\\pilotselo.png")
bird_img = pygame.transform.scale(bird_img, (50, 50))

pipe_img = pygame.image.load("C:\\Users\\YUSUF\\Desktop\\Docs\ \KE\\jpeg\\einstein.jpg" )
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, PIPE_HEIGHT))

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 4
        self.velocity = 0

    def jump(self):
        self.velocity = BIRD_JUMP

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 150)

    def move(self):
        self.x -= BIRD_SPEED

# Main game loop
clock = pygame.time.Clock()
bird = Bird()
pipes = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update bird
    bird.move()

    # Generate pipes
    if len(pipes) == 0 or pipes[-1].x < WIDTH - WIDTH // 2:
        new_pipe = Pipe(WIDTH)
        pipes.append(new_pipe)

    # Update pipes
    for pipe in pipes:
        pipe.move()

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.x > -PIPE_WIDTH]

    # Check for collisions
    for pipe in pipes:
        if (
            bird.x < pipe.x + PIPE_WIDTH
            and bird.x + 50 > pipe.x
            and (bird.y < pipe.height or bird.y + 50 > pipe.height + PIPE_GAP)
        ):
            pygame.quit()
            sys.exit()

    # Draw everything
    window.fill(WHITE)
    window.blit(bird_img, (bird.x, bird.y))

    for pipe in pipes:
        window.blit(pipe_img, (pipe.x, 0))
        window.blit(pipe_img, (pipe.x, pipe.height + PIPE_GAP))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
