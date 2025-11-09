from textual.message import Message

class UserLogin(Message):
    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__()