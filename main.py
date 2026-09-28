from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from Scene import Scene
from Tile import Tile


def draw_scene(scene: Scene, console: tcod.console.Console, width: int = None, height: int = None):

    if(width is None or height is None):
        width = console.width
        height = console.height

    for tile_y in range(height):
        for tile_x in range(width):
            tile: Tile = scene.get_tile(tile_x, tile_y)
            console.print(tile_x, tile_y, tile.glyph)


def main() -> None:
    """Show "Hello World" until the window is closed."""
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tileset += tcod.tileset.procedural_block_elements(shape=tileset.tile_shape)
    console = tcod.console.Console(80, 50)
    console.print(0, 0, "Hello World")  # Test text by printing "Hello World" to the console

    scene = Scene()

    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:  # Main loop
            console.clear()
            draw_scene(scene=scene, console=console)
            context.present(console)  # Render the console to the window and show it
            for event in tcod.event.wait():  # Event loop, blocks until pending events exist
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit


if __name__ == "__main__":
    main()