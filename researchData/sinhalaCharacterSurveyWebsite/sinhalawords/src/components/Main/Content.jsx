import React from 'react';
import Canves from './Canves';
import sinhalaAlphabet from "./../../assets/images/sinhalaAlphabet.jpg";

const Content = () => {
  return (
    <div className="Content_container">
      <div>
          <img src={sinhalaAlphabet} alt="" />
      </div>
      <div className="canves_container">
          <div>sd</div>
          <div><Canves /></div>
          <div>sd</div>
      </div>
    </div>
  );
};

export default Content;
