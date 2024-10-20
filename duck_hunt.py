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