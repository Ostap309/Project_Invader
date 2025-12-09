import pygame as pg
from config import *

from game_screen import GameScreen
from bottom_bar_screen import BtmBarScreen
from image_screen import ImageScreen


class MainScreen:

    def __init__(self) -> None:
        self.main_sur = pg.Surface((MAIN_WIDTH, MAIN_HEIGHT))

        self.game_sc = GameScreen()
        self.btmbar_sc = BtmBarScreen()
        self.image_sc = ImageScreen()

    def update(self) -> None:
        self.game_sc.update()
        self.btmbar_sc.update()
        self.image_sc.update()

        self.main_sur.blit(self.game_sc.game_sur, (0, 0))
        self.main_sur.blit(self.btmbar_sc.btmbar_sur, (0, HEIGHT14))
        self.main_sur.blit(self.image_sc.image_sur, (WIDTH14, HEIGHT14))

    def check_clicks(self, event: pg.event.Event) -> None:
            self.game_sc.check_clicks(event)

    def check_pressed(self, keys: pg.key.ScancodeWrapper) -> None:
        self.game_sc.check_pressed(keys)
