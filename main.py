import pygame
from pygame.locals import *

# import  plauer_hero
# items_attack
# enemes
# блоки (взаимодействие ходить)
#
# инвентарь
pygame.init()

screen = pygame.display.set_mode((1200, 800))

# если класс героя использует атаку,
# мы создаём экземпляр класса оружия
# удаляем его после атаки
# запрещаем создания нового класса оружия, если персонаж атакует
# grooup()


while True:
    screen.fill((255, 255, 255))

    for even in pygame.event.get():
        if even.type == QUIT:
            pygame.quit()


    #класс  персонда  update()

    pygame.display.update()
