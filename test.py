import pygame
pygame.init()

ourScreen = pygame.display.set_mode((400,300))
pygame.display.set_caption('pygame djlee')
finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        pygame.draw.rect(ourScreen, (0,128,255), pygame.Rect(0,0,60,60))
        pygame.display.flip()
