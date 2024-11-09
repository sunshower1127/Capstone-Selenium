import json
import time

from flask import Flask, jsonify
from guardian import get_guardian_articles

app = Flask(__name__)


@app.route("/")
def home():
    return (
        "GET /articles => 기사 가져오기, GET /refresh => 기사 새로고침(3~6초 정도 소요)"
    )


@app.route("/articles")
def articles():
    with open("articles.json") as f:
        data = json.load(f)

    return jsonify(data)


@app.route("/refresh")
def refresh():
    start_time = time.time()
    data = get_guardian_articles()
    with open("articles.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return f"기사 {len(data)}개 수집 완료. {time.time() - start_time:.2f}초 소요."


if __name__ == "__main__":
    app.run(debug=True)
