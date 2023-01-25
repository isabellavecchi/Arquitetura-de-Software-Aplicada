import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import  ReactDOM  from 'react-dom'
import Menu from './components/Menu';
import Home from './components/Home';
import AdminPage from './components/AdminPage';
import Cadastro from './components/Cadastro';
import Login from './components/Login';
import Passagens from './components/Passagens';


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
            <Route path="/admin" element={<AdminPage />} />

            </Routes>

        </div>

        </Router>
    )

        
    
}

ReactDOM.render(<App/>,document.getElementById('root'))