import { useState, useEffect } from "react"
import {getAPI} from '../../services/getStocksList'

const StocksList = () => {
    const [data, setData] = useState([]);
    useEffect(
        () => {
            const getResponse = async () => {
                const response = await getAPI.getStocksList()
                setData(response)                
            }
            getResponse()
            

        }, []
    )
    

    return (
        <section className='w-75 p-2 pb-0 rounded' style={{'backgroundColor': '#6f42c1'}}>
            <table className="table  table-group-divider rounded-1 text-center" style={{  overflow: 'hidden' }}>
            <thead className="table-light">
                <tr>
                    <th scope="col">Paper</th>
                    <th scope="col">Price</th>
                    <th scope="col">Purchase Price</th>
                    <th scope="col">Stock Exchange</th>
                </tr>
            </thead>
            <tbody>
                {data.map((item) => 
                    <tr key={item.paper}>
                        <th scope="row">{item.paper}</th>
                        <td>{item.price}</td>
                        <td>{item.purchase_price}</td>
                        <td>{item.stock_exchange}</td>
                    </tr>
                
                )}
            </tbody>

        </table>
        </section >
    )
}

export default StocksList