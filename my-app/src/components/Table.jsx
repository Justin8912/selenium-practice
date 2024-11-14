const Table = (props) => {
    console.log(props)
    return (
        <>
            <table>
                <tbody>
                    <tr>
                        <td>Section</td>
                        <td>Time</td>
                        <td>Number of Open Seats</td>
                    </tr>
                    {props.sections.map((section)=>(
                        <tr key={section.id}>
                            <td id={section.id} onClick={()=>{props.setDisplay(section.id)}}>{section.id}</td>
                            <td>{section.time}</td>
                            <td>{section.numOfSeats}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    )
}

export default Table;