import React , {useState,useEffect} from 'react'

import "../Styles/Recycle.css"
import Uploader from '../Components/Uploader'
const Recycle = () => {

  return (
    <div className='d-flex justify-content-around errorContainer'>
        <Uploader
        handleChange={(file) => {
        //   var fr = new FileReader();
        //   fr.onload = function () {
        //     TextUpdate(fr.result);
        //   };

        //   fr.readAsText(file);
        
        }}
        handleCancel={(file) => {}}
        name={"file"}
        types={["png","jpg"]}
      />
        
    </div>
  )
}

export default Recycle