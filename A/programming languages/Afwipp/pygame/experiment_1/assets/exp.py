import pygame

pygame.init()

screen = pygame.display.set_mode((0,0))

    


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen, (255,255,255), pygame.rect(10, 10, 10, 10))
    
    
    pygame.display.update()
