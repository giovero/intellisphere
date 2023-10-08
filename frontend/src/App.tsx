import React from "react";
import "./App.css";
import QuizGenerator from "./QuizGenerator";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Classe from "./Classe";
import Sidebar from "./Sidebar";
import Student from "./Student";

function App() {
  return (
    <Router>
      <div className="flex flex-row">
        <Sidebar />
        <div className="ml-[309px] w-full">
          <Routes>
            <Route path="/quiz" element={<QuizGenerator />} />
            <Route path="/quiz/:id" element={<QuizGenerator />} />
            <Route path="/classe" element={<Classe />} />
            <Route path="/classe/:id" element={<Student />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
