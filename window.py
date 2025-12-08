import pygame as pg
from config import *
from main_screen import MainScreen
from utils import ImgLdr


# Класс окна программы
class Window:
    def __init__(self) -> None:
        self.win_sur: pg.Surface = pg.display.set_mode(
            (MAIN_WIDTH, MAIN_HEIGHT),
            pg.RESIZABLE
        )
        ImgLdr.init_stat()

        self.main_sc = MainScreen()
        self.clock = pg.time.Clock()

        pg.display.set_caption("Space Invaders")

    def resize(self, event: pg.event.Event) -> None:
        self.win_sur = pg.display.set_mode(
            (event.w, event.h),
            pg.RESIZABLE
        )

    def centering(self, surface: pg.Surface) -> pg.rect.Rect:
        rect = surface.get_rect()
        rect.center = self.win_sur.get_rect().center
        return rect

    def update(self) -> None:
        self.main_sc.update()

        # Масштабирование изображения
        new_size = min(self.win_sur.get_width(), self.win_sur.get_height())
        scaled_main_surface = pg.transform.scale(
            self.main_sc.main_sur,
            (new_size, new_size)
        )
        self.win_sur.blit(scaled_main_surface, self.centering(scaled_main_surface))
        pg.display.flip()

        self.clock.tick(60)

    def process_keyboard(self, event) -> None:
        self.main_sc.process_keyboard(event)
