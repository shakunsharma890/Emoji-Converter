message = input("Enter your message: ")

message = message.replace(":)", "😊")
message = message.replace(":(", "😢")
message = message.replace(":heart:", "❤️")
message = message.replace(":fire:", "🔥")

print(message)