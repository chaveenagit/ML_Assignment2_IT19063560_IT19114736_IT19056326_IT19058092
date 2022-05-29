import React, { useRef } from "react";
import CanvasDraw from "react-canvas-draw";


function Canves() {
  const canvasRef = useRef(null);

  const ok = () => {
    if (canvasRef.current) {
        console.log(canvasRef.current.canvasContainer.children[1].toDataURL());
      }
  }

  return (
    <div className="App">
      <button onClick={ok}>sddsdsd</button>
      <CanvasDraw
        ref={canvasRef}
        style={{
          boxShadow:
            "0 13px 27px -5px rgba(50, 50, 93, 0.25),    0 8px 16px -8px rgba(0, 0, 0, 0.3)"
        }}
      />
      
    </div>
  );
}

export default Canves;