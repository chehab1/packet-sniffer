import { useEffect } from "react";
import packets from "../packets.json";

function useGetPackets(start,setStart, setPackets){
     function getPackets(){
        try{
            setPackets(packets)
        }catch(err){ 
            console.log(err);
        }finally{
        }

    }
    useEffect(() => {
        if (start)
            getPackets();
    } ,[start]);
}
export default useGetPackets;   