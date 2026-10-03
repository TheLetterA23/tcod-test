from __future__ import annotations

import time

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from Scene import Scene
from SolarSystemScene import SolarSystemScene, Star, Planet
from Tile import Tile
from InputState import InputState

TICK_TIME = 1
TICK_COUNTER = 0

def make_test_scene() -> SolarSystemScene:
    return SolarSystemScene([Star(0,0,4)], [ Planet(
                orbit_radius=5,
                x=5,
                y=0,
                glyph='o',
                color=(180, 180, 180),
            ),
            Planet(
                orbit_radius=9,
                x=0,
                y=9,
                glyph='O',
                color=(100, 160, 255),
            ),
            Planet(
                orbit_radius=13,
                x=-13,
                y=0,
                glyph='O',
                color=(255, 120, 80),
            ),
            Planet(
                orbit_radius=17,
                x=0,
                y=-17,
                glyph='@',
                color=(180, 120, 80),
            ),])


def draw_scene(scene: Scene, console: tcod.console.Console, draw_x: int = 0, draw_y: int = 0, width: int = None, height: int = None, world_x: int = 0, world_y: int = 0):

    if(width is None or height is None):
        width = console.width
        height = console.height

    for tile_y in range(min(height, console.height)):
        for tile_x in range(min(width, console.width)):
            tile: Tile = scene.get_tile(tile_x + world_x, tile_y + world_y)
            console.print(draw_x + tile_x, 
                          draw_y + tile_y, 
                          tile.glyph,
                          fg=tile.fg_color,
                          bg=tile.bg_color)
    console.print(0,0, str(TICK_COUNTER))



def handle_events(input_state: InputState) -> None:
    for event in tcod.event.get():
        print(event)
        if isinstance(event, tcod.event.Quit):
            raise SystemExit
        elif isinstance(event, tcod.event.KeyDown):
            if event.sym == tcod.event.KeySym.ESCAPE:
                raise SystemExit

        input_state.process_event(event=event)
        
def run_tick(tick_counter: int):
    pass

def main() -> None:
    global TICK_COUNTER

    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tileset += tcod.tileset.procedural_block_elements(shape=tileset.tile_shape)
    console = tcod.console.Console(80, 50)
    console.print(0, 0, "Hello World")  # Test text by printing "Hello World" to the console

    scene = make_test_scene()
    input_state = InputState()

    FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED
    with tcod.context.new(console=console, tileset=tileset, sdl_window_flags=FLAGS) as context:
        previous_time = time.perf_counter()
        
        while True:
            console.clear()
            draw_scene(scene=scene, console=console, world_x = -20, world_y = -20)
            context.present(console)
            handle_events(input_state)

            now = time.perf_counter()
            frame_time = now - previous_time

            while frame_time >= TICK_TIME:
                run_tick(TICK_COUNTER)
                frame_time -= TICK_TIME
                TICK_COUNTER += 1

            previous_time = now



if __name__ == "__main__":
    main()

