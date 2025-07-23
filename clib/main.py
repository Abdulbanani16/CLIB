# Rich imports:
from rich.console import Console
from rich.prompt import Prompt

# Prompt toolkit imports:
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings

# Very important values should be here:
important_shit = {
    "?running": True,
    "?prompt": False
}

console = Console()

keyboard = KeyBindings()


@keyboard.add(":")
def command_mode(event):
    global important_shit
    important_shit["?prompt"] = True
    event.app.exit()


@keyboard.add("q")
def quit(event):
    global important_shit
    important_shit["?running"] = False
    event.app.exit()


clib = Application(key_bindings=keyboard)


def main():
    while important_shit["?running"]:
        clib.run()


        if important_shit["?prompt"]:
            command = Prompt.ask("")
            if command in ("q", "quit"):
                console.print("Goodbye :)")
                important_shit["?running"] = False
            else:
                console.print("Fuck you why you type invalid shit >:(")
            important_shit["?prompt"] = False
