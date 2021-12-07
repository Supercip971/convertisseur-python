from typing import Container
import backend 
import sys
from prompt_toolkit import prompt 

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Frame, Label, TextArea


def tui_exit():
    exit()
class Tui(backend.Backend): 
    root_container : Container
    raw_text_area : TextArea
    bin_text_area : TextArea
    hex_text_area : TextArea
    exit_button: Button
    kb: KeyBindings
    def text_updated(self):
        self.bin_text_area.text = "hello"
    def __init__(self):
        pass 

    def run(self):
        self.exit_button = Button("exit", tui_exit)
        self.bin_text_area = TextArea(focusable=True, text="0b0")
        self.hex_text_area = TextArea(focusable=True, text="0x0")
        self.raw_text_area = TextArea(focusable=True, text="0")
        self.root_container = Box(
            HSplit(
                [
                    Label(text="Press `Tab` to move the focus."),
                    VSplit(
                        [
                            Box(
                                body=HSplit([self.exit_button], padding=1),
                                padding=1,
                                style="class:left-pane",
                            ),
                            Box(body=Frame(self.raw_text_area), padding=1, style="class:right-pane"),
                            Box(body=Frame(self.bin_text_area), padding=1, style="class:right-pane"),
                            Box(body=Frame(self.hex_text_area), padding=1, style="class:right-pane"),
                        ]
                    ),
                ]
            ),
        )

        self.layout = Layout(container=self.root_container, focused_element=self.exit_button)
        
        
        # Key bindings.
        self.kb = KeyBindings()
        self.kb.add("tab")(focus_next)
        self.kb.add("s-tab")(focus_previous)

        # Styling.
        self.style = Style(
            [
                ("left-pane", "bg:#880000 #000000"),
                ("right-pane", "bg:#aa0000 #000000"),
                ("button", "#000000"),
                ("button-arrow", "#000000"),
                ("button focused", "bg:#ff0000"),
                ("text-area focused", "fg:#ffffff"),
            ]
        )

        self.application = Application(layout=self.layout, key_bindings=self.kb, style=self.style, full_screen=True)

        self.application.run()
        

    def draw(self):
        pass
    def update(self) -> backend.CalValue: 
        pass

    def exit(self): 
        pass
