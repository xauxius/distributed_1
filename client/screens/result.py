from textual.screen import Screen
from textual.reactive import reactive
from textual.widgets import Header, Footer, Log
from textual.app import ComposeResult

from state import app_state

class ResultScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Log()
        yield Footer()

    