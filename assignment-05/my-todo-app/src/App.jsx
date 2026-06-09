import { useState } from "react";

function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");

  const addTodo = () => {
    if (input.trim() === "") return;

    setTodos([...todos, input]);
    setInput("");
  };

  const deleteTodo = (indexToDelete) => {
  setTodos(todos.filter((_, index) => index !== indexToDelete));
  };


  return (
    <div style={{ textAlign: "center", marginTop: "40px" }}>
      <h2>Simple Todo App</h2>

      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter todo"
      />

      <button onClick={addTodo}>Add</button>

      <ul>
        {todos.map((todo, index) => (
          <li key={index}>{todo}</li>
        ))}
      </ul>

      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo}
              <button onClick={() => deleteTodo(index)}>Delete</button>
          </li>
        ))}
      </ul>

    </div>
  );
}

export default App;
