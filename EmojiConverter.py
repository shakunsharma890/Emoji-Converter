import json

# Load emoji data from JSON file
with open("emoji_map.json", "r", encoding="utf-8") as file:
    emoji_map = json.load(file)


def convert_message(message):
    # Replace longer shortcuts first
    for shortcut in sorted(emoji_map, key=len, reverse=True):
        message = message.replace(shortcut, emoji_map[shortcut])

    return message


def reverse_convert_message(message):
    # Replace longer emoji strings first
    for shortcut, emoji in sorted(
        emoji_map.items(),
        key=lambda item: len(item[1]),
        reverse=True
    ):
        message = message.replace(emoji, shortcut)

    return message

if __name__ == "__main__":
    Message = input("Enter your Message:- ")
    print(convert_message(Message))