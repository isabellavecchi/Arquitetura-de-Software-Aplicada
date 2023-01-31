import React, { useState } from 'react';
// import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button'
import * as ReactBootStrap from 'react-bootstrap';
import {voos} from './AdminTickets';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';


export const renderVoos = (voo, index) => {
  return(
    <tr key={index}>
      <td>{voo.id}</td>
      <td>{voo.partida}</td>
      <td>{voo.destino}</td>
      <td>{voo.diaP}</td>
      <td>{voo.horarioP}</td>
      <td>{voo.diaC}</td>
      <td>{voo.horarioC}</td>
      <td>{voo.valor}</td>
      
    </tr>

  )

}

export const renderVoosSelect = (voo, index) => {
  return(
   
  <option value={voo.id}>De {voo.partida} à {voo.destino} no dia: {voo.dia} as {voo.horario} por {voo.valor}   </option>
    
   

  )

}


const Passagens=()=>{
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  
return(
    <div className="container  d-flex align-items-center flex-column mt-5">
     <p>Lista de aeroportos com passagens disponíveis</p>
        <div className='m-2'>
        <Button variant="success" onClick={handleShow}>Comprar passagem</Button>
        </div>
        {/* <ReactBootStrap.Table></ReactBootStrap.Table> */}
        <ReactBootStrap.Table striped bordered hover className='text-center' >
      <thead>
        <tr>
          <th>id</th>
          <th>Partida</th>
          <th>Destino</th>
          <th>Data Partida</th>
          <th>Horario de Partida</th>
          <th>Data chegada</th>
          <th>Horario de Chegada</th>
          <th>valor</th>
        </tr>
      </thead>
      <tbody>
       {/* {
          posts.blogs && posts.blogs.map((item) => (
        <tr key={item.id}>
          <td>{item.id}</td>
          <td>{item.title}</td>
          <td>{item.body}</td>
          <td> 
          <Button className='mx-1' variant="info"><FaPen color="white" /></Button>
          <Button className='mx-1' variant="danger"><AiOutlineClose /> </Button>
          </td>
        </tr>
          ))
        } */}
   
        {voos.map(renderVoos)}

        
      
      </tbody>
    </ReactBootStrap.Table>

    <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Comprar passagem</Modal.Title>
        </Modal.Header>
        <Modal.Body>Selecione qual passagem deseja comprar
        <Form.Select aria-label="Default select example">
      <option>Vôos disponiveis</option>
      {voos.map(renderVoosSelect)}
      {/* <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option> */}
        </Form.Select>

        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Comprar mais tarde
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Comprar passagem
          </Button>
        </Modal.Footer>
      </Modal>
   
        
    </div>
)

}

export default Passagens