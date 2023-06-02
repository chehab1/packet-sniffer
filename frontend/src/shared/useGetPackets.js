import { useEffect } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import packets from "../packets.json";

let GlobalPackets = [];
let connection = null;
function useGetPackets(
  start,
  setPackets,
  state,
  setState,
  loading,
  setLoading
) {
  function getPackets() {
    setLoading(true);
    if (!connection)
      connection = new W3CWebSocket(
        "ws://127.0.0.1:8000/ws/" + "socket-server" + "/"
      );

    connection.onopen = () => {
      console.log("WebSocket Client Connected");
    };
    connection.onmessage = (message) => {
      const dataFromServer = JSON.parse(message.data);

      if (dataFromServer) {
        setLoading(false);

        setState((state) => ({
          messages: dataFromServer,
        }));
        console.log(dataFromServer);
        GlobalPackets.push(dataFromServer);
        setPackets(GlobalPackets);
      }
    };
  }
  useEffect(() => {
    if (start) getPackets();
    else {
      if (connection) connection.close();
      GlobalPackets = [];
      connection = null;
      if (packets.length) setPackets([]);
    }
  }, [start]);
}
export default useGetPackets;
