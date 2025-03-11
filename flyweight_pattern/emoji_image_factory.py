from emoji_image import EmojiImage


class EmojiImageFactory:
    _images = {}

    @classmethod
    def get_image(cls, file_name: str) -> EmojiImage:
        if file_name not in cls._images:
            cls._images[file_name] = EmojiImage(file_name)
        return cls._images[file_name]

    @classmethod
    def get_all_images(cls):
        return cls._images
