import time

from article_collector import get_guardian_articles
from data_manager import get_article, get_articles_headers, write_articles
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return (
        "<h1>캡스톤 프로젝트 서버</h1>"
        "<p>아래 경로로 GET 요청을 보내면 JSON 형식으로 값을 반환해줌.</p>"
        "<p>모든 데이터는 문자열이고 자동으로 한글로 번역돼서 제공됨.</p>"
        "<ol>"
        "   <li>/article - 모든 기사 헤더 반환 ( [{ title, subtitle, author, date }] )</li>"
        "   <li>/article/:index - 해당 인덱스(0~length-1)의 기사 반환. 처음엔 번역되느라 느릴 수 있음 ( { title, subtitle, author, date, body } )</li>"
        "   <li>/update - 기사 새로 가져오기 (새로운 기사만 가져와서 새로운 기사가 많을수록 느림. 4초 ~ 15초)</li>"
        "</ol>"
    )


@app.route("/article")
def articles():
    return jsonify(get_articles_headers())


@app.route("/article/<int:index>")
def article(index: int):
    return jsonify(get_article(index))


@app.route("/update")
def update():
    start_time = time.time()
    articles = get_guardian_articles()
    write_articles(articles)

    return f"기사 {len(articles)}개 수집 완료. {time.time() - start_time:.2f}초 소요."


if __name__ == "__main__":
    app.run(debug=True)
