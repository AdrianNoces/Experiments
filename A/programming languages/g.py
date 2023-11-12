import pygame
import sys
import random
import time

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player properties
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# Obstacle properties
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 3

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("gg")

# Function to handle events (e.g., closing the game)
def handle_events():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
# Function to create obstacles
def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    y = -OBSTACLE_HEIGHT
    return pygame.Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
            
# Main game loop
def main():
    player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    obstacles = []
    clock = pygame.time.Clock()
    
    while True:
        handle_events()
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        dx = mouse_x - player.centerx
        dy = mouse_y - player.centery
        
        if dx != 0 or dy != 0:
                distance = max(abs(dx), abs(dy))
                ratio = PLAYER_SPEED / distance
                dx *= ratio
                dy *= ratio
                
        player.move_ip(dx, dy)
        
        player.left = max(player.left, 0)
        player.right = min(player.right, SCREEN_WIDTH)
        player.top = max(player.top, 0)
        player.bottom = min(player.bottom, SCREEN_HEIGHT)
      	  
        # Move obstacles and create new one
        for obstacle in obstacles[:]:
        	obstacle.y += OBSTACLE_SPEED
        	if obstacle.y > SCREEN_HEIGHT:
        		obstacles.remove(obstacle)
      	    
        if len(obstacles) < 5:  # Limit the number of obstacles on the screen
            obstacles.append(create_obstacle())
                     
        # Collision detection
        for obstacle in obstacles:
        	if player.colliderect(obstacle):
        		screen.fill(WHITE)
        		print("\nyou have shitty gaming skill\n"*5)
        		time.sleep(2)
        		pygame.quit()
        		sys.exit()
                
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        for obstacle in obstacles:
        	pygame.draw.rect(screen, WHITE, obstacle)
        pygame.display.flip()
                                            
        clock.tick(60)  # 60 frames per second
        
if __name__ == "__main__":
 	main()
      	    
            
            
