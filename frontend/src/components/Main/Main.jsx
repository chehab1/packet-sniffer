import Packets from "../Packets/Packets";
import PacketInfo from "../PacketInfo/PacketInfo";
import {useState} from 'react';

function Main({ start }) {
    let [index, setIndex] = useState(0);
    return (
        <>
        {start && (
            <div style={{ marginTop: '150px' }}>
            <Packets {...{setIndex}} />
            <PacketInfo {...{index}} />
            </div>
        )}
        </>
    );
}

export default Main;
