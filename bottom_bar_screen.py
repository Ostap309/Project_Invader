import pygame as pg
from config import *
from utils import ImgLdr


class BtmBarScreen:

    def __init__(self):

        self.btmbar_sur = pg.Surface((WIDTH14, HEIGHT3))

    def update(self):
        self.btmbar_sur.blit(ImgLdr.dict["btmbar"], (0, 0))
