async function getStocksList() {
    try {
        const conn = await fetch('http://127.0.0.1:8000/stocks/')
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

export const getAPI = {
    getStocksList
}

getStocksList()