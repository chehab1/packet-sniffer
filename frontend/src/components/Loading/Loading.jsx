import { useState } from "react";
import dog from "../../dog-sniffer.jpg";
import "./styles.css";

function Loading() {
  let [pos , setPos] = useState(0);
  setTimeout(() => {
     let x = pos;
      x += 1;
      if (x == 1420) x = 0;
      document.getElementById("dogImage").style.left = x + "px";
      setPos(x);
  },5);
  return (
    <div id="dogImage">
      <img src={dog} alt="dog" width={100} height={100} />
    </div>
  );
}
export default Loading;

{
  /* <div className="spinner-border " role="status">
<span className="sr-only">

</span> 
</div> */
}
