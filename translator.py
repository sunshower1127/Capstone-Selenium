import os
from datetime import datetime

import pytz
from babel.dates import format_datetime
from deepl import Translator
from dotenv import load_dotenv

load_dotenv()

deepl_key = os.getenv("DEEPL_KEY")
if not deepl_key:
    msg = "DEEPL_KEY is not set in the environment variables."
    raise ValueError(msg)

translator = Translator(deepl_key)


def translate_one(text: str):
    translated = translator.translate_text(text, source_lang="EN", target_lang="KO")
    if isinstance(translated, list):
        raise TypeError
    return translated.text


def translate_many(*texts: str):
    translated = translator.translate_text(texts, source_lang="EN", target_lang="KO")
    if isinstance(translated, list):
        return [t.text for t in translated]
    raise TypeError


def translate_date(date_text: str):
    date_text = date_text.replace(".", ":")

    # 날짜 텍스트를 datetime 객체로 파싱
    date_format = "%a %d %b %Y %H:%M %Z"
    date_obj = datetime.strptime(date_text, date_format)

    # GMT 시간대를 pytz를 사용하여 설정
    gmt = pytz.timezone("GMT")
    date_obj = gmt.localize(date_obj)

    # 한국 시간대로 변환
    kst = pytz.timezone("Asia/Seoul")
    date_obj_kst = date_obj.astimezone(kst)

    # 한국어로 날짜 포맷
    formatted_date = format_datetime(
        date_obj_kst, "y년 M월 d일 EEEE a h시 m분", locale="ko_KR"
    )

    formatted_date = formatted_date.replace("AM", "오전").replace("PM", "오후")

    return formatted_date


if __name__ == "__main__":
    print(translate_one("Hello, world!\nThis is a test."))
    print(translate_date("Fri 17 Dec 2021 4:00 GMT"))
