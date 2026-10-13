import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return <main><h1>Hello World from React + Docker!</h1><p>The React bundle is served by Nginx.</p></main>;
}

createRoot(document.getElementById("root")).render(<App />);
