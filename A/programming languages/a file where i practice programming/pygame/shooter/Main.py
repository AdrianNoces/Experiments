import pygame
import os
pygame.init()

# / * SCREEN * \

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('shooting game')

# / * DEFINE PLAYER ACTION VARIABLES * \

moving_left = False
moving_right = False

# SET FRAMERATE
clock = pygame.time.Clock()
fps = 120

# DEFINE COLOURS
BG = (144, 201, 120)

def draw_bg():
    screen.fill(BG)

# / * PLAYER * \

class player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load('images/player/idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
            
            
        if moving_right:
            dx = self.speed  
            self.flip = False
            self.direction = 1
            
        self.rect.x += dx
        self.rect.y += dy
        
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)

psoldier = player(200, 200, 1, 10)



# / * WHILE EVENTS IS RUNNING AND UPDATING * \
if run = False:
    print("window quit")
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # / * KEYBOARD PRESSES  * \ 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True   
            if event.key == pygame.K_RIGHT:
               moving_right = True 
            if event.key == pygame.K_ESCAPE:
                run = False




    # / * KEYBOARD PRESSES  * \ 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                 moving_right = False
                 
                 
        clock.tick(fps)
        draw_bg()
        psoldier.draw()
        psoldier.move(moving_left, moving_right)
                
    pygame.display.update()      
pygame.quit()
