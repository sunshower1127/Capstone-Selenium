# 환경 관련 기사 가져오는 모듈

3학년 2학기 캡스톤 프로젝트
Selenium으로 The Guardian의 Cliamte Crisis 탭의 최신 기사들을 크롤링해서,
Flask 서버에서 JSON 형태로 제공해줌.

```shell
python server.py
cloudflared tunnel --url http://127.0.0.1:5000
```

/articles -> 기사 가져오기 (json으로 리턴)
/refresh -> 기사 새로고침 (하나당 2초정도 소요)