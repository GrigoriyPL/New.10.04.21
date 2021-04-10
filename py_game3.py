import pygame

x,y = 250, 250
W, H = 500, 500

pygame.init()
sc = pygame.display.set_mode((W,H))
color = (255,255,255)
fps = pygame.time.Clock()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill((0,0,0))
    x += 1 
    if x > W:
        x = 0

    pygame.draw.circle(sc, color, (x, y), 25)
    fps.tick(60)
    pygame.display.update()