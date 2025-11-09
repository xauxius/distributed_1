from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, DirectoryTree, Footer

from config import config

class ImageSelectorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield DirectoryTree(config.IMAGES_PATH)
        yield Footer()

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        print(event.path)