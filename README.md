# 환경 관련 기사 가져오는 모듈

3학년 2학기 캡스톤 프로젝트
Selenium으로 The Guardian의 Cliamte Crisis 탭의 최신 기사들을 크롤링해서,
Flask 서버에서 JSON 형태로 제공해줌.

```shell
python server.py
cloudflared tunnel --url http://127.0.0.1:5000
```

해서 내가 서버 주소를 줄거임.

---

## API 설명

아래 경로로 GET 요청을 보내면 JSON 형식으로 값을 반환해줌.
모든 데이터는 문자열이고 자동으로 한글로 번역돼서 제공됨.

1. `/article` - 모든 기사 헤더 반환 (`[{ title, subtitle, author, date }]`)
2. `/article/:index` - 해당 인덱스(0~length-1)의 기사 반환. 처음 가져오는건 번역되느라 느릴 수 있음 (`{ title, subtitle, author, date, body }`)
3. `/update` - 기사 새로 가져오기 (새로운 기사만 가져와서 새로운 기사가 많을수록 느림. 4초 ~ 15초)

---

## API 사용 예시(더 자세한 예시는 Fetch-Test 참고)

```javascript
const URL = "https://내가건네준주소";

// 모든 기사 헤더를 가져오는 함수
async function getAllArticles() {
  try {
    const response = await fetch(`${URL}/article`);
    const articles = await response.json();
    return articles;
  } catch (error) {
    console.error("Error fetching article headers:", error);
  }
}

// 특정 인덱스의 기사를 가져오는 함수
async function getArticle(index) {
  try {
    const response = await fetch(`${URL}/article/${index}`);
    const article = await response.json();
    return article;
  } catch (error) {
    console.error(`Error fetching article at index ${index}:`, error);
  }
}

// 기사를 새로 가져와서 서버의 데이터를 업데이트 시키는 함수
async function updateArticles() {
  try {
    const response = await fetch(`${URL}/update`);
    if (!response.ok) {
      console.error("Error updating articles:", response.status);
    }
  } catch (error) {
    console.error("Error updating articles:", error);
  }
}

// 함수 호출 예시
async function main() {
  await updateArticles();
  console.log("기사 업데이트 완료");

  const articles = await getAllArticles();
  console.log("모든 기사 가져오기 완료");
  console.log(articles);

  const article = await getArticle(4);
  console.log("5번째 기사 가져오기 완료");
  console.log(article);
}

main();
```
