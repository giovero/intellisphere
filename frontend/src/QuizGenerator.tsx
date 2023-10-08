import React, { ReactNode, useEffect, useState } from "react";
import "./App.css";
import ArrowRight from "./assets/ArrowRight";
import { useParams } from "react-router-dom";

const QuizGenerator = () => {
  const { id } = useParams();

  const examples = [
    "10 domande di scienze per una classe di prima elementare sull'argomento degli animali e dei loro habitat",
    "Per una classe di seconda media, generami domande di geografia riguardanti i continenti e i loro principali paesi e capitali",
    "Mi servono domande di lingua italiana per una classe di quarta elementare sull'argomento della grammatica e delle parti del discorso.",
  ];
  const [quiz, setQuiz] = useState("");
  const [searchText, setSearchText] = useState("");
  const [student, setStudent] = useState<any>();
  const Card = ({ children }: { children: ReactNode }) => {
    return (
      <div className="border bg-[#E8E8E8] flex flex-col gap-4 p-4 rounded-2xl shadow-md">
        {children}
      </div>
    );
  };

  const handleClick = async () => {
    const endpoint = "http://127.0.0.1:5000/search_text?";
    const searchParams = new URLSearchParams();

    searchParams.append("all_text", searchText);
    if (id) {
      searchParams.append("alunno_id", id);
    }

    try {
      const response = await fetch(endpoint + searchParams);
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "quiz.pdf";
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      } else {
        console.error("Error downloading PDF");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  useEffect(() => {
    const fetchUser = async () => {
      const searchParams = new URLSearchParams();

      searchParams.append("alunno_id", id || "");

      const endpoint = "http://127.0.0.1:5000/get_students?" + searchParams;
      const response = await fetch(endpoint);
      const data = await response.json();
      if (data.result.length) {
        setStudent({
          ...data.result[0],
          media: (Math.random() * (10 - 5) + 5).toFixed(1),
        });
      }
    };
    if (id) {
      fetchUser();
    } else {
      setStudent(undefined);
    }
  }, [id]);

  return (
    <div className="flex flex-col m-16 gap-4">
      <h2 className="text-2xl font-semibold mb-4">
        Genera quiz per {student?.name || "Classe 2^A"}
      </h2>
      <div className="border bg-[#E8E8E8] flex flex-col gap-4 p-4 rounded-2xl shadow-md">
        <label className="block text-[#1C1C1C] text-sm font-bold mb-2">
          Descrivi il tuo quiz:
        </label>
        <textarea
          className=" rounded-lg w-full p-2 px-1 border border-gray-300"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
        />
        <div>
          <button
            disabled={searchText.length === 0}
            onClick={handleClick}
            className="bg-[#1C1C1C] text-xs text-white font-bold py-4 px-6 rounded-full"
          >
            Genera quiz
          </button>
        </div>
      </div>
      <div className="flex flex-row gap-4">
        {examples.map((text, index) => (
          <Card key={index}>
            <div className="text-[#1C1C1C] font-bold">{text}</div>
            <div className="flex flex-row items-end justify-end h-full">
              <button
                type="submit"
                onClick={() => setSearchText(text)}
                className="bg-[#1C1C1C] w-fit text-white font-bold py-2 px-4 rounded-full"
              >
                <div className="w-6 h-6">
                  <ArrowRight />
                </div>
              </button>
            </div>
          </Card>
        ))}
      </div>
      {!!quiz.length && (
        <Card>
          <div className="rounded p-16">{quiz}</div>
        </Card>
      )}
    </div>
  );
};

export default QuizGenerator;
