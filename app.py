from flask import Flask, request, render_template, jsonify
from trans import trans_ja2en
from create_image import create_image

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        career = request.form["career"]
        tastes = request.form["tastes"]
        character = request.form["character"]

        en_words = trans_ja2en(career=career, tastes=tastes, character=character)
        return render_template("result.html", en_words=en_words)


@app.route("/generate_image", methods=["POST"])
def generate_image():
    en_words = request.form.getlist("en_words[]")
    j, t = create_image(prompt="\n".join(en_words))
    if j:
        return jsonify({"file_name": t})
    else:
        return jsonify({"error": f"Error: {t}"})


if __name__ == "__main__":
    app.run(debug=True)
