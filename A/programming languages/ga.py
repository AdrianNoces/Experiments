import pygame
import sys
import random

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
pygame.display.set_caption("Simple Pygame Game")

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
                                                                        
                                                                                # Move the player
                                                                                        keys = pygame.key.get_pressed()
                                                                                                if keys[pygame.K_LEFT] and player.left > 0:
                                                                                                            player.x -= PLAYER_SPEED
                                                                                                                    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
                                                                                                                                player.x += PLAYER_SPEED
                                                                                                                                
                                                                                                                                        # Move obstacles and create new ones
                                                                                                                                                for obstacle in obstacles[:]:
                                                                                                                                                            obstacle.y += OBSTACLE_SPEED
                                                                                                                                                                        if obstacle.y > SCREEN_HEIGHT:
                                                                                                                                                                                        obstacles.remove(obstacle)
                                                                                                                                                                                        
                                                                                                                                                                                                if len(obstacles) < 5:  # Limit the number of obstacles on the screen
                                                                                                                                                                                                            obstacles.append(create_obstacle())
                                                                                                                                                                                                            
                                                                                                                                                                                                                    # Collision detection
                                                                                                                                                                                                                            for obstacle in obstacles:
                                                                                                                                                                                                                                        if player.colliderect(obstacle):
                                                                                                                                                                                                                                                        print("Game Over")
                                                                                                                                                                                                                                                                        pygame.quit()
                                                                                                                                                                                                                                                                                        sys.exit()
                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                # Draw everything
                                                                                                                                                                                                                                                                                                        screen.fill(BLACK)
                                                                                                                                                                                                                                                                                                                pygame.draw.rect(screen, WHITE, player)
                                                                                                                                                                                                                                                                                                                        for obstacle in obstacles:
                                                                                                                                                                                                                                                                                                                                    pygame.draw.rect(screen, WHITE, obstacle)
                                                                                                                                                                                                                                                                                                                                            pygame.display.flip()
                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                    clock.tick(60)  # 60 frames per second
                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                        main()
                                                                                                                                                                                                                                                                                                                                                        
