from doctest import debug

import pygame as pg


class SpriteAnimation:
    def __init__(self, frames, frame_delay_ms, cyclic=False, debug=False):
        self.frames = frames
        self.frame_delay = frame_delay_ms
        self.current_frame = -1
        self.last_update = pg.time.get_ticks()
        self.is_playing = True
        self.cyclic = cyclic

        self.debug = debug

    def update(self):
        if not self.is_playing:
            return
        current_time = pg.time.get_ticks()
        if current_time - self.last_update > self.frame_delay:
            if self.cyclic:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
            else:
                if self.current_frame < len(self.frames) - 1:
                    self.current_frame += 1
                else:

                    print("Выключение") if self.debug else None
                    self.is_playing = False
            print(self.current_frame, self.frames[self.current_frame]) if self.debug else None
            self.last_update = current_time

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def play(self):
        print("Старт") if self.debug else None
        self.is_playing = True
        self.current_frame = -1

    def stop(self):
        self.is_playing = False
