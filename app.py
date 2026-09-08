from flask import Flask, render_template, request
from EmojiConverter import convert_message, reverse_convert_message, emoji_map

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    result = ""

    if request.method == "POST":
        message = request.form.get("message", "")

        if request.form.get("action") == "reverse":
            result = reverse_convert_message(message)
        else:
            result = convert_message(message)

    return render_template(
        "index.html",
        message=message,
        result=result,
        emoji_map=emoji_map
    )


if __name__ == "__main__":
    app.run(debug=True)