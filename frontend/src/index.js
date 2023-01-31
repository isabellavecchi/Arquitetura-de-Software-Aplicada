import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import  ReactDOM  from 'react-dom'
import Menu from './components/Menu';
import Home from './components/Home';
import AdminPassports from './components/AdminPassports';
import Cadastro from './components/Cadastro';
import Login from './components/Login';
import Passagens from './components/Passagens';
import AdminClients from './components/AdminClients'
import AdminAirports from './components/AdminAirports'
import './styles/styles.css'


import{BrowserRouter as Router,Routes,Route} from 'react-router-dom'


const App=()=>{

    return(
        <Router>
             <Menu/>
        <div className="container">
           
            <Routes>
            <Route path="/" exact element={<Home />} />
            <Route path="/produtos" element={<Cadastro />} />
            <Route path="/login" element={<Login />} />
            <Route path="/passagens" element={<Passagens />} />
            <Route path="/cadastro" element={<Cadastro />} />
            <Route path="/adminP" element={<AdminPassports />} />
            <Route path="/adminC" element={<AdminClients />} />
            <Route path="/adminA" element={<AdminAirports />} />
            </Routes>

        </div>

        </Router>
    )

        
    
}

ReactDOM.render(<App/>,document.getElementById('root'))