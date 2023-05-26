import "./styles.css";
import { useContext } from 'react';
import { PacketsContext }  from '../../contexts/packetsContext';

function PacketInfo({index}) {
    let {packets,setPackets} = useContext(PacketsContext);
    console.log(packets);
    // let packetInfo = packets[index].Info;
    return (
        <div className="packet-info">
        <h1>PacketInfo</h1>
        {
            packets.length && 
            <div>
                <h3>Ethernet</h3>
                <p>dst: {packets[index].Info.Ethernet.dst}</p>
                <p>src: {packets[index].Info.Ethernet.src}</p>
                <p>type: {packets[index].Info.Ethernet.type}</p>
                <h3>Payload</h3>
                <p>{packets[index].payload}</p>
            </div>
        }
        </div>
    );
}

export default PacketInfo;
