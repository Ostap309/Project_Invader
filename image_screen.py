import pygame as pg
from config import *


class ImageScreen:
    display_image = None

    @staticmethod
    def init_stat():
        ImageScreen.display_image = pg.image.load("assets/display_image.png").convert_alpha()

    def __init__(self):
        ImageScreen.init_stat()

        self.image_sur = pg.Surface((WIDTH3, HEIGHT3))

    def update(self):
        self.image_sur.blit(self.display_image, (0, 0))
