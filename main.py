import pygame as pg
from window import Window

# Инициализация pygame
pg.init()

# Создание окна приложения
window = Window()

#  Отслеживание статуса
running = True

# Жизненный цикл
while running:

    # Отслеживание событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.VIDEORESIZE:
            # Обновляем размер окна при изменении
            window.resize(event)
        elif event.type == pg.KEYDOWN:
            window.process_keyboard(event.key)

    # Обновление окна
    window.update()
