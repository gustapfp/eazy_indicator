import StocksList from "../StocksList/StocksList";
import AddStockButton from '../AddStockButton/AddStockButton'

const HomePage = () => {
    return (
        <section >

            <div className=" container d-flex flex-row-reverse m-4">
                <AddStockButton> New Stock </AddStockButton>
            </div>
            <div className="container d-flex justify-content-center align-items-center mt-5 ">
                <StocksList />
            </div>
        </section>

    )

}

export default HomePage;

