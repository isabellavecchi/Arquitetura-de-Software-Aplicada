import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import  ReactDOM  from 'react-dom'
import Menu from './components/Menu';
import Home from './components/Home';
import AdminTickets from './components/AdminTickets';
import Cadastro from './components/Cadastro';
import Login from './components/Login';
// import Passagens from './components/Passagens';
import AdminPassagens from './components/AdminPassagens';
import AdminAirports from './components/AdminAirports';
// import UserPage from './components/UserPage';
import './styles/styles.css';

import{BrowserRouter as Router,Routes,Route} from 'react-router-dom'


const App=()=>{

    return(
        <Router>
             <Menu/>
        <div className="container">
           
            <Routes>
            <Route path="/" exact element={<Home />} />
            <Route path="/login" element={<Login />} />
            {/* <Route path="/passagens" element={<Passagens />} /> */}
            <Route path="/cadastro" element={<Cadastro />} />
            <Route path="/adminT" element={<AdminTickets />} />
            <Route path="/adminC" element={<AdminPassagens />} />
            <Route path="/adminA" element={<AdminAirports />} />
            {/* <Route path="/userP" element={<UserPage />} /> */}
            </Routes>

        </div>

        </Router>
    )

        
    
}

ReactDOM.render(<App/>,document.getElementById('root'))