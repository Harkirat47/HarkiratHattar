import pygame
import sys

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Kiss Animation')

clock = pygame.time.Clock()

# Load images (replace 'path_to_image1.png' and 'path_to_image2.png' with your image paths)
image1 = pygame.image.load('kiss.png')
image2 = pygame.image.load('kiss.png')

# Scale images to fit the screen (adjust if needed)
image1 = pygame.transform.scale(image1, (100, 100))
image2 = pygame.transform.scale(image2, (100, 100))

image1_rect = image1.get_rect(center=(width // 4, height // 2))
image2_rect = image2.get_rect(center=(width * 3 // 4, height // 2))

kissing = False
kiss_count = 0

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press space to trigger the kiss
                kissing = True

    if kissing:
        kiss_count += 1
        if kiss_count < 60:  # Duration of the kiss (adjust as needed)
            image1_rect.y -= 1
            image2_rect.y -= 1
        else:
            kissing = False
            kiss_count = 0
            image1_rect.y += 1
            image2_rect.y += 1

    screen.blit(image1, image1_rect)
    screen.blit(image2, image2_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
