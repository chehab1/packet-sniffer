import "./styles.css";
import useGetPackets from "../../shared/useGetPackets";
import { useContext } from 'react';
import { PacketsContext }  from '../../contexts/packetsContext';


function Header({ start, setStart }) {
    
    let {packets,setPackets} = useContext(PacketsContext);
    useGetPackets(start, setStart, setPackets);

    return (
        <div className="row d-flex justify-content-center Header">
        <h1 className="col-12">Network Packet Sniffer</h1>
        {!start && (
            <button id="start" className="col-12" onClick={() => setStart(!start)}>
            Start Sniffing
            </button>
        )}
        {start && (
            <button id="stop" className="col-12" onClick={() => setStart(!start)}>
            Stop Sniffing
            </button>
        )}
        </div>
    );
}

export default Header;
