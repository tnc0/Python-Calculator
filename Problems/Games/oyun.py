import pygame

WIDTH = 1366        
HEIGHT = 768
pygame.display.set_caption("Flappy Bird", "UTF-8")

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("C:\\Users\\YUSUF\\Desktop\\KE\\jpeg\\pilotselo.png")
screen.blit(background, (0, 0))

game_over_image = pygame.image.load("C:\\Users\\YUSUF\\Desktop\\KE\\jpeg\\einstein.jpg")

bird = pygame.Rect(100, 100, 50, 50)

pipe1 = pygame.Rect(200, 0, 100, 200)
pipe2 = pygame.Rect(300, 0, 100, 200)
game_over = False  # Oyunun başlangıçta devam ettiğini belirtmek için

while True:
    pygame.display.update()

    if bird.colliderect(pipe1) or bird.colliderect(pipe2) or bird.bottom <= 0:
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass

    if game_over:
        screen.blit(game_over_image, (0, 0))
