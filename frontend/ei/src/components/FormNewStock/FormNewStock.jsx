import { useState } from "react"
import { postAPI } from "../../services/postStock"

const FormNewStock = () => {

    const [paper, setPaper] = useState()
    const [price, setPrice] = useState()
    const [purchase_price, setPurchasePrice] = useState()
    const [stock_exchange, setStockExchange] = useState()

    function onSubmit() {
        const newStock = {
            "price": price,
            "purchase_price": purchase_price,
            "paper": paper,
            "stock_exchange": stock_exchange
        }

        postAPI.postNewStock(newStock)

    }
    return (
        <div className="container d-flex justify-content-center align-items-center vh-100">
            <div className=' w-75 p-5'>

            <form className="bg-secondary-subtle rounded p-5">
                <div className="mb-3">
                    <label htmlFor="paper" className="form-label">Paper</label>
                    <input onChange={(event)=>{setPaper(event.target.value)}} type="text" className=" form-control" id="purchase_price" placeholder="Stock tag: ITUB4"></input>
                </div>
                <div className="mb-3">
                    <label htmlFor="price" className="form-label">Price</label>
                    <input 
                    onChange={(event)=>{setPrice(event.target.value)}} type="text" className="form-control" id="price" placeholder="Price today"></input>
                </div>
                <div className="mb-3">
                    <label htmlFor="purchase_price" className="form-label">Purchase Price</label>
                    <input 
                    onChange={(event)=>{setPurchasePrice(event.target.value)}} type="text" className="form-control" id="Price when the stock was purchase" placeholder="Another input placeholder"></input>
                </div>
                <div className="mb-3">
                    <label htmlFor="stock_exchange" className="form-label">Stock Exchange</label>
                    <input 
                    onChange={(event)=>{setStockExchange(event.target.value)}} type="text" className="form-control" id="stock_exchange" placeholder="The Stock Exchange where the paper belongs."></input>
                </div>
                <div className="text-center pt-3 pb-1"> 
                    <button onClick={()=> {onSubmit()}} className="btn w-50 text-white" type="submit" value="Submit" style={{'backgroundColor': '#6f42c1'}}>Add Stock</button>

                </div>

            </form>
            </div>
        </div>

    )
}

export default FormNewStock;