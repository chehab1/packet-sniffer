import "./App.css";
import Header from "./components/Header/Header";
import Main from "./components/Main/Main";
import { PacketsContext } from "./contexts/packetsContext";
import { useState } from "react";

function App() {
  let [start, setStart] = useState(false);
  let [packets, setPackets] = useState([]);

  return (
    <div className="App container">
      <PacketsContext.Provider value={{ packets, setPackets }}>
        <Header {...{ start, setStart }} />
        <Main {...{ start }} />
      </PacketsContext.Provider>
    </div>
  );
}

export default App;
