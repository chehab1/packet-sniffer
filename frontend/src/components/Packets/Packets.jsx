import "./styles.css";
import Icon from "@mui/material/Icon";
import { useContext } from 'react';
import { PacketsContext }  from '../../contexts/packetsContext';

function Packets({setIndex}) {
  let {packets,setPackets} = useContext(PacketsContext);

  return (
    <>
    {
      packets.length > 0
      &&
    <div className="tableContainer">
      <table className="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Protocol</th>
            <th scope="col">SrcIP</th>
            <th scope="col">SrcPrt</th>
            <th scope="col">DstIP</th>
            <th scope="col">DstPrt</th>
            {/* <th scope="col">Length</th> */}
            <th scope="col">status</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {packets.map((packet) => {
              return (
                <tr variant="success" key = {packet.no}>
                <th scope="row">{packet.no}</th>
                <td>{packet.Protocol}</td>
                <td>{packet.SrcIP}</td>
                <td>{packet.SrcPrt}</td>
                <td>{packet.DstIP}</td>
                <td>{packet.DstPrt}</td>
                <td>{packet.status}</td>
                <td>
                  <button onClick={() => setIndex(packet.no)}>
                    <Icon>add_circle</Icon>
                  </button>
                </td> 
                </tr>
              )
          })}
       
        </tbody>
      </table>
    </div>
}
    </>
  );
}

export default Packets;
