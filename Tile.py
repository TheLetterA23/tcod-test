from dataclasses import dataclass

@dataclass
class Tile:
    glyph: str
    fg_color: tuple[int, int, int] = (255, 255, 255)
    bg_color: tuple[int, int, int] = (0, 0, 0)