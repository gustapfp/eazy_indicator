
import './App.css';
import {BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom'

import 'bootstrap/dist/css/bootstrap.css'; 
import HomePage from './components/HomePage/HomePage';
import FormNewStock from './components/FormNewStock/FormNewStock';

function App() {
  return (
    <Router>
      <Routes>
        <Route
          path='/'
          element={
            <HomePage/>
          }
        />
        <Route
        path='/new-stock'
        element={
          <FormNewStock/>
        }
        />
      </Routes>
    </Router>

  );
}

export default App;
