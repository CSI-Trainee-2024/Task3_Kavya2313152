import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
BLUE = (135, 206, 235) 
BLACK = (0, 0, 0)
MAX_MISSES = 3 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Duck Hunt")
clock = pygame.time.Clock()
duck_image = pygame.image.load('duck.png')

class Duck:
    def __init__(self):
        self.image = duck_image
        self.reset()

    def draw(self, surface):
        if self.is_visible:
            surface.blit(self.image, (self.x, self.y))

    def reset(self):
        self.x = random.randint(0, WIDTH - self.image.get_width())
        self.y = random.randint(50, HEIGHT // 2)
        self.is_visible = True

def main():
    duck = Duck()
    score = 0
    misses = 0
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if duck.is_visible:
                    if duck.x < mouse_x < duck.x + duck.image.get_width() and duck.y < mouse_y < duck.y + duck.image.get_height():
                        duck.is_visible = False  
                        score += 1  
                        duck.reset()  
                    else:
                        misses += 1 

        if misses >= MAX_MISSES:  
            running = False  

        screen.fill(BLUE) 
        duck.draw(screen)  

        score_text = font.render(f'Score: {score}', True, BLACK)
        misses_text = font.render(f'Misses: {misses}', True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(misses_text, (10, 50))

        pygame.display.flip()  
        clock.tick(FPS)  

    screen.fill(BLUE)  
    final_message = 'Game Over! You missed too many ducks.'
    final_score_text = font.render(final_message, True, BLACK)
    screen.blit(final_score_text, (WIDTH // 4, HEIGHT // 2))
    final_score_display = font.render(f'Final Score: {score}', True, BLACK)
    screen.blit(final_score_display, (WIDTH // 4, HEIGHT // 2 + 50))
    pygame.display.flip()
    pygame.time.wait(3000) 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
