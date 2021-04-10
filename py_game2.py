import pygame
j = 0
i = 0
color = (255, 255, 255)

pygame.init()
sc = pygame.display.set_mode((500,500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()        
    for i in range(10):
        pygame.draw.ellipse(sc,color,(i * 15, 0, 500 - i * 30, 500), 1)
    for j in range(10):
        pygame.draw.ellipse(sc,color,(0, j * 15, 500, 500 - j * 30,), 1)
        pygame.display.update()