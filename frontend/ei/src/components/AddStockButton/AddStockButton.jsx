import {useNavigate} from 'react-router-dom'

// Cria uma variave com o useNavigate



const AddStockButton = (props) => {
    const navigate = useNavigate()
    return(
        <button onClick={()=> {navigate('/new-stock', {replace: true})}} className="btn text-white" type="submit" value="Submit" style={{'backgroundColor': '#6f42c1'}}>{props.children}</button>
    )

}

export default AddStockButton