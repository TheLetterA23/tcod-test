import tcod.event

class InputState:
    def __init__(self):
        self.held = set()
        self.commands = []

    def process_event(self, event: tcod.event.Event):
        if isinstance(event, tcod.event.KeyDown):
            self.held.add(event.sym)

            if event.sym == tcod.event.KeySym.UP:
                self.commands.append(("move", 0, -1))
            elif event.sym == tcod.event.KeySym.DOWN:
                self.commands.append(("move", 0, 1))
            elif event.sym == tcod.event.KeySym.LEFT:
                self.commands.append(("move", -1, 0))
            elif event.sym == tcod.event.KeySym.RIGHT:
                self.commands.append(("move", 1, 0))

        elif isinstance(event, tcod.event.KeyUp):
            self.held.discard(event.sym)

    def consume_commands(self):
        commands = self.commands
        self.commands = []
        return commands
