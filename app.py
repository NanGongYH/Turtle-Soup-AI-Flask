from flask import Flask, render_template, request, jsonify
import json, time

app = Flask(__name__)

# 载入题库
with open("data/riddles.json", "r", encoding="utf-8") as f:
    riddles = json.load(f)


@app.route("/")
def index():
    return render_template("index.html", riddles=riddles)


@app.route("/mode/<int:riddle_id>")
def mode(riddle_id):
    return render_template("mode.html", riddle_id=riddle_id)


@app.route("/game/<int:riddle_id>/<mode>")
def game(riddle_id, mode):
    riddle = next((r for r in riddles if r["id"] == riddle_id), None)
    return render_template("game.html", riddle=riddle, mode=mode)


# AI 判定接口（你未来改成火山方舟）
def ai_judge(question, truth):
    """
    这里先占位，返回固定值，
    你以后换成火山方舟的 API。
    """
    return "是（示例占位）"


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data["question"]
    truth = data["truth"]

    answer = ai_judge(question, truth)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
