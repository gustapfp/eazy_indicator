async function postNewStock(data) {
    try {
        const conn = await fetch('http://127.0.0.1:8000/stocks/add_stock', {
            method:'POST', 
            headers: {
                "Content-type":"application/json"
            },
            body:JSON.stringify({
                price: data.price,
                purchase_price: data.purchase_price,
                paper: data.paper,
                stock_exchange: data.stock_exchange
        })
        }
        )
        const stocks = await conn.json()
        return stocks

    } catch (error) {
        return (
            <div className="alert alert-danger d-flex align-items-center" role="alert">
                <svg className="bi flex-shrink-0 me-2" role="img" aria-label="Danger:"><use xlinkHref="#exclamation-triangle-fill" /></svg>
                <div>
                    {error}
                </div>
            </div>
        )
    }
}

export const postAPI = {
    postNewStock
}

postNewStock()