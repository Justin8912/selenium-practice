import './App.css';
import Table from "./components/Table.jsx";
import SizeChanger from './components/SizeChanger.jsx';
import { useState } from 'react';

function App() {
  const [ display, setDisplay ] = useState(0);

  const [ sections, setSections ] = useState([
    {
      id: "41352",
      time: "M 10:30am - 4:30am",
      numOfSeats: 0
    },
    {
      id: "41355",
      time: "M 10:30am - 4:30pm",
      numOfSeats: 0
    },
    {
      id: "41360",
      time: "M 12:30pm - 4:30pm",
      numOfSeats: 0
    },
    {
      id: "41365",
      time: "M 12:30pm - 4:30pm",
      numOfSeats: 0
    },
    {
      id: "41370",
      time: "M 12:30pm - 4:30pm",
      numOfSeats: 0
    }
  ])

  const setSectionSeatNumber = (sectionId, numOfSeats) => {
    let newSections = sections.map(element => {
      if (element.id === sectionId) {
        element.numOfSeats = numOfSeats
      }
      return element;
    })

    setSections(newSections)
    setDisplay(0);
  }

  return (
    <>
     {
      display === 0 ?
        <div className="App">
          <Table 
            setDisplay={setDisplay}
            sections={sections}
          ></Table>
        </div> :
        <SizeChanger
          section={display}
          submitHandler={setSectionSeatNumber}
        />
      }
    </>
  );
}

export default App;
