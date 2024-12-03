import { useRef, useState } from "react";

export default function SingleArticle() {
  const rf = useRef(null);
  const [data, setData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const articleNum = rf.current.value - 1;
      const res = await fetch(`http://localhost:8080/article/${articleNum}`);
      const jsn = await res.json();
      setData(jsn);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <section className="btn">
      <form onSubmit={handleSubmit}>
        <input type="number" ref={rf} min="1" max="99" required />
        <button type="submit">번째기사 보기</button>
      </form>
      {data && (
        <div className="article">
          <h2>{data.title}</h2>
          <h3>{data.subtitle}</h3>
          <p>
            {data.author} | {data.date}
          </p>
          <p>{data.body}</p>
        </div>
      )}
    </section>
  );
}
