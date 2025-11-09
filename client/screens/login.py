from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Input

from .result import ResultScreen
from state import app_state

class LoginScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Input()
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted):
        app_state.username = event.value
        print()
        self.app.push_screen(ResultScreen())