from Tile import Tile

import tcod.console

class Scene:
    def __init__(self):
        pass

    def get_tile(self, x: int, y: int) -> Tile:
        return Tile(glyph='X')