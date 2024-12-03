import "./App.css";
import AllArticles from "./components/AllArticles";
import SingleArticle from "./components/SingleArticle";
import UpdateArticle from "./components/UpdateArticle";

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
