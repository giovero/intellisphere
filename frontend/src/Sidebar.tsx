import React from "react";
import { useNavigate } from "react-router-dom";

const Sidebar = () => {
  const navigate = useNavigate();

  return (
    <div className="bg-black text-white fixed left-0 top-0 w-[309px] h-screen">
      <div className="flex flex-col p-6">
        <div className="text-lg font-bold">Bentornata, Giulia</div>
        <div className="mt-28 flex flex-col gap-3">
          <div
            className="p-4 rounded-lg"
            style={{
              backgroundColor:
                window.location.pathname === "/classe" ? "#434343" : "black",
            }}
            onClick={() => navigate("/classe")}
          >
            Classe
          </div>
          <div
            className="p-4 rounded-lg"
            style={{
              backgroundColor:
                window.location.pathname === "/quiz" ? "#434343" : "black",
            }}
            onClick={() => navigate("/quiz")}
          >
            Quiz
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
