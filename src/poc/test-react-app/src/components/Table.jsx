const Table = (props) => {
    return (
        <>
            <table>
                <tbody>
                    <tr>
                        <th>Section</th>
                        <th>Time</th>
                        <th>Number of Open Seats</th>
                    </tr>
                    { props.sections.map((section) => (
                        <tr key={section.id}>
                            <th id={section.id} onClick={ ()=>{props.setDisplay(section.id)} }><a>{section.id}</a></th>
                            <td>{section.time}</td>
                            <td>{section.numOfSeats}</td>
                        </tr>
                    )) }
                </tbody>
            </table>
        </>
    )
}

export default Table;