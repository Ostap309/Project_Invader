import pygame as pg


class ImgLdr:
    dict = {}

    @staticmethod
    def init_stat():
        ImgLdr.dict = {
            "BG_space1": pg.image.load('assets/space/space1.png').convert_alpha(),
            "BG_space2": pg.image.load('assets/space/space2.png').convert_alpha(),
            "BG_space3": pg.image.load('assets/space/space3.png').convert_alpha(),

            "btmbar": pg.image.load("assets/btmbar_image.png").convert_alpha(),
            "iconbar": pg.image.load("assets/display_image.png").convert_alpha(),

            "spaceship_move0": pg.image.load('assets/spaceship_image_1.png').convert_alpha(),
            "spaceship_move1": pg.image.load('assets/spaceship_image_2.png').convert_alpha(),
            "spaceship_move2": pg.image.load('assets/spaceship_image_3.png').convert_alpha(),
            "spaceship_move3": pg.image.load('assets/spaceship_image_4.png').convert_alpha(),

            "spaceship_braking0": pg.image.load('assets/spaceship_braking_1.png').convert_alpha(),
            "spaceship_braking1": pg.image.load('assets/spaceship_braking_2.png').convert_alpha(),
            "spaceship_braking2": pg.image.load('assets/spaceship_braking_3.png').convert_alpha(),
            "spaceship_braking3": pg.image.load('assets/spaceship_braking_4.png').convert_alpha()

        }
