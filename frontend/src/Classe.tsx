import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Classe = () => {
  const [students, setStudents] = useState([]);
  const navigate = useNavigate();
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchList = async () => {
      const endpoint = "http://127.0.0.1:5000/get_students";
      const response = await fetch(endpoint);
      const data = await response.json();
      setStudents(
        data.result.map((s: any) => {
          s.average = (Math.random() * (10 - 5) + 5).toFixed(1);
          return s;
        })
      );
    };
    fetchList();
  }, []);

  return (
    <div className="flex flex-col w-full gap-4 p-16">
      <div className="flex flex-row w-full justify-between">
        <div className="font-bold text-4xl">Classe 2^A</div>
        <input
          className="bg-[#E8E8E8] p-2 rounded-full"
          placeholder="Cerca studente..."
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>
      <div className="flex gap-4 flex-wrap">
        {students
          .filter((s: any) =>
            s.name.toLowerCase().includes(search.toLowerCase())
          )
          .map((student: any) => (
            <div className="border rounded-2xl max-w-[329px] flex flex-col divide-y">
              <div className="flex flex-row gap-2 items-center p-4 flex-nowrap">
                <div className="font-bold break-words text-2xl text-[#1C1C1C]">
                  {student.name}
                </div>
                <img
                  width={240}
                  height={240}
                  alt={student.name}
                  src={student.image_url}
                />
              </div>
              <div className="flex flex-row justify-between py-3 px-4">
                <div>{student.average} media</div>
                <button
                  onClick={() => navigate(`/classe/${student.id}`)}
                  className="bg-[#1C1C1C] text-xs text-white font-bold py-2 px-3 rounded-full"
                >
                  visualizza
                </button>
              </div>
            </div>
          ))}
        <div className=""></div>
      </div>
    </div>
  );
};

export default Classe;
