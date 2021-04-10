import pygame

x,y =100, 100
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
    # sc.fill((0,0,0))
    # x += 1 
    # if x > W:
    #     x = 0

    keys = pygame.key.get_pressed() # перемещение с клавиатуры
    if keys [pygame.K_DOWN]:
        y += 1
        if y > H:
            y = 0

    if keys [pygame.K_UP]:
        y -= 1
        if y > H:
            y = 0

    if keys [pygame.K_RIGHT]:
        x += 1
        if x > W:
            x = 0

    if keys [pygame.K_LEFT]:
        x -= 1
        if x > W:
            x = 0

        if keys[ pygame.K_ESCAPE]:
            exit()
    pygame.draw.circle(sc, color, (x, y), 25)
    fps.tick(144)
    pygame.display.update()