from typing import Dict
from rich.console import Console
from rich.text import Text
import random

class CLIB:
    def __init__(self, header_dict: Dict[str, str] | None = None) -> None:
        self.running = True
        self.console = Console()
        self.header = self.make_header(header_dict) if header_dict else self.make_header()

    def make_header(self, header_dict: Dict[str, str] | None = None):
        header = Text()
        if header_dict:
            for text, style in header_dict.items():
                header.append(text, style)
        else:
            header_str = """_________ .____    ._____________ 
\\_   ___ \\|    |   |   \\______   \\
/    \\  \\/|    |   |   ||    |  _/
\\     \\___|    |___|   ||    |   \\
 \\______  /_______ \\___||______  /
        \\/        \\/           \\/"""
            styles = ["red", "yellow", "green", "blue", "cyan", "pink", "purple"]

            for line in header_str.strip("\n").splitlines():
                header.append(line, random.choice(styles))
                header.append("\n")

        return header
    
    def mainloop(self):
        self.console.print(self.header)
        while self.running:
            smth = input("> ")
            if smth == "clear" or smth == "x":
                self.console.clear()
            elif smth == "quit" or smth == "q":
                self.running = False
            else:
                print(f"Ok {smth}")
