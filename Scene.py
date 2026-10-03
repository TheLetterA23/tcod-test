from Tile import Tile

import tcod.console

class Scene:
    def __init__(self):
        pass

    def get_tile(self, x: int, y: int) -> Tile:
        return Tile(glyph=str(y)[0], bg_color=(255,0,255))