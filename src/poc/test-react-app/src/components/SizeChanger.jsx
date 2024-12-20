import { useState } from 'react';

const SizeChanger = (props) => {
    const [currentDisplay, setCurrentDisplay] = useState("display");

    const [ userInput, setUserInput ] = useState(0);
    return (
        <>
        {
            currentDisplay === "display" ?
            <div id='totalSeats'>
                <button onClick={()=>{setCurrentDisplay("edit")}}>Edit</button>
            </div>
            :
            <div id="totalSeatsForm" className>
                <p>Please select the number of seats you would like for {props.section}</p>
                <input id="seatsInput" type="textArea" onChange={ (e)=>{
                    setUserInput(e.target.value);
                } }></input>
                <button className="seats-btn" onClick={ ()=>{
                    setCurrentDisplay("display")
                    props.submitHandler(props.section, userInput)
                } }>Submit</button>
            </div>

        }
            
        </>
    )
}

export default SizeChanger;
