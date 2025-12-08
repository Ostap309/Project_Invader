import pygame as pg
from window import Window

# Инициализация pygame
pg.init()
# Инициализация микшера
pg.mixer.init()
# Загрузка музыкального файла
pg.mixer.music.load('assets/Space_-_Voices_Of_Jupiter.mp3')
# Запуск воспроизведения (бесконечно)
pg.mixer.music.play(loops=-1)

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
        elif event.type == pg.KEYDOWN or event.type == pg.KEYUP:
            window.process_keyboard(event)

    # Обновление окна
    window.update()
