import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((0, 0))

background = pygame.image.load("images/bg1.jpeg")

run = True
while run:
    
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            
    pygame.display.update()
    clock.tick(60)