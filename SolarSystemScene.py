from dataclasses import dataclass, field
import random

from Tile import Tile
from Scene import Scene
import math

@dataclass
class Star:
    x: int
    y: int
    radius: int
    tile: Tile = field(default_factory=lambda: Tile(glyph='*', fg_color=(255,255,0)))

    def is_point_inside(self, px: int, py: int):
        return math.dist((px, py), (self.x, self.y)) < self.radius

@dataclass
class Planet:
    orbit_radius: int
    x: int
    y: int
    glyph: str
    color: tuple[int, int, int]

    def is_point_inside(self, px: int, py: int) -> bool:
        return px == self.x and py == self.y

    def is_on_orbit(self, px: int, py: int) -> bool:
        distance = math.dist((px, py), (0, 0))
        return abs(distance - self.orbit_radius) < 0.6

    @property
    def tile(self) -> Tile:
        return Tile(
            glyph=self.glyph,
            fg_color=self.color,
            bg_color=(0, 0, 0),
        )

class SolarSystemScene(Scene):

    def __init__(self, stars: list[Star] | None = None, planets: list[Planet] | None = None):
        super().__init__()
        self.stars = stars if stars is not None else []
        self.planets = planets if planets is not None else []
        self.empty_space_glyph = ' '
        self.distant_star_glyph = '.'

    def get_tile(self, x: int, y: int) -> Tile:
        for star in self.stars:
            if star.is_point_inside(x, y):
                return star.tile

        for planet in self.planets:
            if planet.is_point_inside(x, y):
                return planet.tile
            
            if planet.is_on_orbit(x, y):
                return Tile(
                    glyph='·',
                    fg_color=(70, 70, 70),
                    bg_color=(0, 0, 0),
                )
        random.seed(str(x) + '_' + str(y))
        if random.random() > 0.99:
            return Tile(glyph=self.distant_star_glyph, bg_color=(0,0,0), fg_color=(100,100,random.randint(0,100)))
        else:
            return Tile(glyph=self.empty_space_glyph, bg_color=(0,0,0))
            
            
    