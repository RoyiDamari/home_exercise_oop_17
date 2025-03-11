from emoji import Emoji
from emoji_image_factory import EmojiImageFactory


def main():
    # Create 2 "angry" emojis
    angry_emoji1 = Emoji(name="Angry", size=32, image_file="angry.png")
    angry_emoji2 = Emoji(name="Angry2", size=16, image_file="angry.png")

    # Create 2 "heart eye" emojis
    heart_emoji1 = Emoji(name="Heart Eye", size=32, image_file="heart_eye.png")
    heart_emoji2 = Emoji(name="Heart Eye2", size=64, image_file="heart_eye.png")

    # Create 2 "thinking" emojis
    thinking_emoji1 = Emoji(name="Thinking", size=32, image_file="thinking.png")
    thinking_emoji2 = Emoji(name="Thinking2", size=64, image_file="thinking.png")

    # Print them out
    print(angry_emoji1)
    print(angry_emoji2)
    print(heart_emoji1)
    print(heart_emoji2)
    print(thinking_emoji1)
    print(thinking_emoji2)

    # Check how many distinct images we have in the factory
    all_images = EmojiImageFactory.get_all_images()
    print("\nAll images in factory:", all_images)
    print("Number of distinct images:", len(all_images))


if __name__ == "__main__":
    main()
