class EmojiImage:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return f"EmojiImage({self.file_name})"
