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
