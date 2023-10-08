import React, { useEffect } from "react";
import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import ArrowLeft from "./assets/ArrowLeft";

const Student = () => {
  const { id } = useParams();
  const [student, setStudent] = useState<any>();
  const [editable, setEditable] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    console.log(id);
    const fetchStudent = async () => {
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
      fetchStudent();
    }
  }, [id]);

  const updateStudent = async () => {
    const searchParams = new URLSearchParams();

    searchParams.append("alunno_id", id || "");

    const endpoint = "http://127.0.0.1:5000/update_alunno";
    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        alunno_id: student.id,
        additional_req: student.additional_req,
      }),
    });
    const data = await response.json();
    console.log(data.result);
    if (data.result) {
      setEditable(false);
    }
  };

  if (!student) return <></>;
  return (
    <div className="flex flex-col gap-4 p-16 w-full">
      <button
        className="bg-transparent text-xs text-black font-bold py-4 px-6 rounded-full"
        onClick={() => navigate(-1)}
      >
        <ArrowLeft />
      </button>
      <div className="flex flex-row gap-6 items-center">
        <img
          width={120}
          height={120}
          alt={student.name}
          src={student.image_url}
        />
        <div className="flex flex-col gap-6">
          <div>Classe 2^A</div>
          <div className="font-bold break-words text-3xl text-[#1C1C1C]">
            {student.name}
          </div>
          <div>{student.media} media</div>
        </div>
      </div>
      {editable ? (
        <textarea
          className=" rounded-lg w-full p-2 px-1 border border-gray-300"
          value={student.additional_req}
          onChange={(e) =>
            setStudent({ ...student, additional_req: e.target.value })
          }
        />
      ) : (
        <div className="text-[#666666]">{student.additional_req}</div>
      )}
      <div className="flex flex-row gap-4">
        <button
          onClick={() => setEditable(!editable)}
          className="bg-[#1C1C1C] text-xs text-white font-bold py-2 px-3 rounded-full"
        >
          {editable ? "Annulla" : "Modifica descrizione"}
        </button>
        {editable && (
          <button
            onClick={updateStudent}
            disabled={!editable}
            className="bg-[#1C1C1C] text-xs text-white font-bold py-2 px-3 rounded-full"
          >
            Salva modifiche
          </button>
        )}
      </div>
      <div>
        <button
          onClick={() => navigate("/quiz/" + student.id)}
          className="bg-[#1C1C1C] text-xs text-white font-bold py-2 px-3 rounded-full"
        >
          Crea quiz personalizzato
        </button>
      </div>
    </div>
  );
};

export default Student;
