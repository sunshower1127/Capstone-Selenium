import "./App.css";
import AllArticles from "./AllArticles";
import SingleArticle from "./SingleArticle";
import UpdateArticle from "./UpdateArticle";

function App() {
  return (
    <div className="container">
      <UpdateArticle />
      <AllArticles />
      <SingleArticle />
    </div>
  );
}

export default App;
