import {useState} from 'react';

const SizeChanger = (props) => {
    const [userInput, setUserInput] = useState(0);
    return (<>
        <p>Please select the number of seats you would like for {props.section}</p>
        <input id="setSeatNumber" type="textArea" onChange={(e)=>{
            setUserInput(e.target.value);
        }}></input>
        <button onClick={()=>{props.submitHandler(props.section, userInput)}}>Submit</button>
    </>)
}

export default SizeChanger;
