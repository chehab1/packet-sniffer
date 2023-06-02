import "./styles.css";
import { useContext } from "react";
import { PacketsContext } from "../../contexts/packetsContext";

function PacketInfo({ index }) {
  let { packets, setPackets } = useContext(PacketsContext);
  return (
    <>
      {packets.length > 0 && (
        <div className="packet-info">
          <h1>PacketInfo</h1>

          <div>
            <h3>Ethernet</h3>
            <p>dst: {packets[index].Info.Ethernet.dst}</p>
            <p>src: {packets[index].Info.Ethernet.src}</p>
            <p>type: {packets[index].Info.Ethernet.type}</p>
            <h3>Payload</h3>
            <p>{packets[index].Payload ? packets[index].Payload :"No Payload" }</p>
          </div>
        </div>
      )}
    </>
  );
}

export default PacketInfo;
