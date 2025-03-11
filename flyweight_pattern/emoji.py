from emoji_image_factory import EmojiImageFactory


class Emoji:

    def __init__(self, name: str, size: int, image_file: str):
        self.name = name
        self.size = size
        # Instead of creating a new EmojiImage, we request one from the factory
        self.image = EmojiImageFactory.get_image(image_file)

    def __repr__(self):
        return (f"Emoji(name={self.name}, size={self.size}, "
                f"image={self.image.file_name})")
