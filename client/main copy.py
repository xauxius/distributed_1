# from PIL import Image
# import requests
from dotenv import load_dotenv
import os
import sys

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DirectoryTree
from textual.screen import Screen

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL") or sys.exit("No API URL")
IMAGES_PATH = os.getenv("IMAGES_PATH") or sys.exit("No images path")

class LoginScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

class ImageSelectorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield DirectoryTree(IMAGES_PATH)
        yield Footer()

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        print(event.path)

class ResultScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

class Client(App):
    BINDINGS = [
        ("a", "analyze_image", "Analyze image"),
        ("v", "view_results", "View Results"),
        ("r", "refresh", "Refresh")
        ]


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