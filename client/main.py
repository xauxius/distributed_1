# from PIL import Image
# import requests
from dotenv import load_dotenv
import os
import sys

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DirectoryTree, Input, Log
from textual.screen import Screen
from textual.message import Message
from textual.reactive import reactive

from screens import LoginScreen, ImageSelectorScreen, ResultScreen

class Client(App):
    data: str = "None"

    BINDINGS = [
        ("a", "analyze_image", "Analyze image"),
        ("v", "view_results", "View Results"),
        ("r", "refresh", "Refresh")
        ]
    
    def on_mount(self) -> None:
        self.push_screen(LoginScreen())

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_analyze_image(self) -> None:
        self.switch_screen(ImageSelectorScreen())

    def action_view_results(self) -> None:
        self.switch_screen(ResultScreen())
    

if __name__ == "__main__":
    app = Client()
    app.run()