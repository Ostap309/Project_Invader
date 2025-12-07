import pygame as pg
from config import *


class BtmBarScreen:
    btmbar_image = None

    @staticmethod
    def init_stat():
        BtmBarScreen.btmbar_image = pg.image.load("assets/btmbar_image.png").convert_alpha()

    def __init__(self):
        BtmBarScreen.init_stat()

        self.btmbar_sur = pg.Surface((WIDTH14, HEIGHT3))

    def update(self):
        self.btmbar_sur.blit(BtmBarScreen.btmbar_image, (0, 0))
