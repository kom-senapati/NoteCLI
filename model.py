class Note:
    def __init__(self, title, content, position=None) -> None:
        self.title = title
        self.content = content
        self.position = position

    def __repr__(self) -> str:
        return f"({self.title}, {self.content}, {self.position})"
