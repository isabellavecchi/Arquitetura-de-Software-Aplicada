import React from 'react'
import Button from 'react-bootstrap/Button';
import { NavLink } from "react-router-dom";

const Home=()=>{
return(
    <div className="container d-flex align-items-center flex-column text-center mt-5">
       <h3>
       Seja Bem vindo!
       </h3> 
       <h6>Deseja iniciar a sessão?</h6>
       <Button style={{ width: "100px"}} as={NavLink} to="/login" className='' variant="success">Entrar</Button>{' '}
               
    </div>
)

}

export default Home