import pathlib
from pathlib import Path

class Settings:
    def __init__(self):
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.fps = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship.png'
        self.ship_w = 40
        self.ship_h = 60