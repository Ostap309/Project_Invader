import pygame as pg
from config import *
from utils import ImgLdr


class ImageScreen:
    def __init__(self):
        self.image_sur = pg.Surface((WIDTH3, HEIGHT3))

    def update(self):
        self.image_sur.blit(ImgLdr.dict["iconbar"], (0, 0))
