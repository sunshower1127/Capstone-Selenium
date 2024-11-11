import "./style.css";

const URL = "https://pro-strips-bon-dedicated.trycloudflare.com/";

const button = document.querySelector("button");
const logContainer = document.getElementById("log");
const articlesContainer = document.getElementById("articles");
const articleContainer = document.getElementById("article");

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

async function handleClick() {
  await updateArticles();
  logContainer.textContent += "기사 업데이트 완료\n";

  const articles = await getAllArticles();
  logContainer.textContent += "모든 기사 가져오기 완료\n";
  articlesContainer.textContent = JSON.stringify(articles, null, 2);

  const article = await getArticle(4);
  logContainer.textContent += "5번째 기사 가져오기 완료\n";
  articleContainer.textContent = JSON.stringify(article, null, 2);
}

button.addEventListener("click", handleClick);
