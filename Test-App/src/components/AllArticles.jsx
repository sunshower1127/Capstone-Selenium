import { useState } from "react";

export default function AllArticles() {
  const [data, setData] = useState(null);

  const handleClick = async () => {
    try {
      const res = await fetch("http://localhost:8080/article");
      const jsn = await res.json();
      setData(jsn);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <section className="btn">
      <button onClick={handleClick}>전체 기사 보기</button>
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </section>
  );
}
