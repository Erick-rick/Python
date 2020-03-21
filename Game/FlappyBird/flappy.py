import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT= 800

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image =[pygame.image.load('img/bluebird-upflap.png').convert_alpha(),
                     pygame.image.load('img/bluebird-midflap.png').convert_alpha(),
                     pygame.image.load('img/bluebird-downflap.png').convert_alpha()
                    ]

        self.current_image = 0

        self.image = pygame.image.load('img/bluebird-midflap.png').convert_alpha() #convert_alpha -- excluir pixels transparentes
        
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH /2
        self.rect[1] = SCREEN_HEIGHT/2
    

    def update(self):
        self.current_image= (self.current_image + 1)% 3
        self.image = self.image[self.current_image]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('img/background-night.png')
#BACKGROUND - pygame.tranform.scale(BACKGROUND,(SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird =Bird()
bird_group.add(bird)

clock = pygame.tiem.Clock()

while True:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    #posição de imagem / plano cardesiano
    screen.blit(BACKGROUND,(0, 0)) 

    bird_group.update()
    bird_group.draw(screen)

    pygame.display.update()