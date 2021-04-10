# pip install pygame - установка через командную строку

import pygame # подключение модуля

color = (255, 255, 125) # Политра РГБ

pygame.init() # инициализация pygame
sc = pygame.display.set_mode((500, 500)) # создание окна .display вывод окна .set_mode(()) указанные параметры

running = True
while running: # не дает закрыться окну
    for event in pygame.event.get(): # ожидается действие
        if event.type == pygame.QUIT: # Закрытие окна
            exit()
    #pygame.display.set_caption("First window") # переимнование окна .set_caption
    sc.fill(color) # делает заливку данным цветом можно задать цвет напрямую sc.Fill((30,255,8)) обязательны двойные скобки
    pygame.draw.circle(sc, (0,0,0),(250,250),200,150) # draw - нарисовать circle - объект color - цвет (250, 250) - координаты 200 - радиус 5 - Толщина
    pygame.display.update() # обновление экрана 
    