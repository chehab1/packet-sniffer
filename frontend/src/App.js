import "./App.css";
import Header from "./components/Header/Header";
import Main from "./components/Main/Main";
import { PacketsContext } from "./contexts/packetsContext";
import { useState } from "react";
import useGetPackets from "./shared/useGetPackets";
import Loading from "./components/Loading/Loading";


function App() {
  let [start, setStart] = useState(false);
  let [packets, setPackets] = useState([]);
  let [loading, setLoading] = useState(true);
  let [state, setState] = useState({
    filledForm: false,
    messages: [],
    value: "",
    name: "",
    room: "socket-server",
  });

  useGetPackets(start, setPackets, state, setState,loading, setLoading);
  

  return (
    <div className="App container">
      {
      <PacketsContext.Provider value={{ packets, setPackets }}>
        <Header {...{ start, setStart }} />
        <Loading />
        {/* {(loading || !loading) && start &&<Loading />} */}
        {start &&  <Main {...{ start }} />}

      </PacketsContext.Provider>
      }
    </div>
  );
}

export default App;
