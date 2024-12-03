import { useState } from "react";

export default function UpdateArticle() {
  const [message, setMessage] = useState("");

  const handleClick = async () => {
    try {
      await fetch("http://localhost:8080/article/update");
      setMessage("완료됐습니다!");
    } catch (err) {
      console.error(err);
      setMessage("업데이트 중 오류가 발생했습니다.");
    }
  };

  return (
    <section className="btn">
      <button onClick={handleClick}>업데이트하기</button>
      <p>{message}</p>
    </section>
  );
}
