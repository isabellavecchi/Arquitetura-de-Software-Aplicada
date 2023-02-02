import React from 'react'
import Button from 'react-bootstrap/Button';
import { NavLink } from "react-router-dom";
import { useAuth } from "../auth";
const LoggedOutLinks = () => {
    return (
        <>
        <div className="container d-flex align-items-center flex-column text-center mt-5">
       <h3>
       Seja Bem vindo a AviaTur!
       </h3> 
       <h6>Deseja iniciar a sessão?</h6>
       <Button style={{ width: "100px"}} as={NavLink} to="/login" className='' variant="success">Entrar</Button>{' '}
               
    </div>
        </>
    )
  }
  const LoggedInLinks = () => {
    return (
        <> 
          <div className="container d-flex align-items-center flex-column text-center mt-5">
       <h3>
       Seja Bem vindo de volta!
       </h3> 
       <h6>Oque você deseja fazer?</h6>
       <div className='d-flex justify-between'>
       <Button  as={NavLink} to="/adminT" className='m-1' variant="success">Administrar Voos</Button>{' '}
       <Button  as={NavLink} to="/adminP" className='m-1' variant="secondary">Administrar Passagens</Button>{' '}
       <Button  as={NavLink} to="/adminA" className='m-1' variant="primary">Administrar Aeroportos</Button>{' '}       
       </div>
        </div>
        </>
    )
  }





const Home=()=>{
    const [logged]=useAuth();
return(
    <div>
      {logged?<LoggedInLinks/>:<LoggedOutLinks/>}
    </div>

)

}

export default Home