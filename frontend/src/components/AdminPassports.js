import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import Modal from 'react-bootstrap/Modal';
import { InputGroup } from 'react-bootstrap';
import * as ReactBootStrap from 'react-bootstrap';
import Form from 'react-bootstrap/Form';


export const voos = [
  {id:"1",partida:"uberlandia", destino:"sao paulo", dia:"22/07/2023", horario:"19:00", valor:"250,00"},
  {id:"2",partida:"sao paulo", destino:"uberlandia", dia:"24/07/2023", horario:"10:00", valor:"340,00"},
  {id:"3",partida:"belo horizonte", destino:"sao paulo", dia:"20/07/2023", horario:"13:00", valor:"370,00"},
  {id:"4",partida:"uberlandia", destino:"bahia", dia:"21/07/2023", horario:"9:00", valor:"650,00"}
]

export const renderVoos = (voo, index) => {
  return(
      <tr key={index}>
      <td>{voo.id}</td>
      <td>{voo.partida}</td>
      <td>{voo.destino}</td>
      <td>{voo.dia}</td>
      <td>{voo.horario}</td>
      <td>{voo.valor}</td>
      <td> 
        <Button className='mx-1' variant="info"><FaPen color="white" /></Button>
        <Button className='mx-1' variant="danger"><AiOutlineClose /> </Button>
        </td>
    </tr>

  )

}


const AdminPassports=()=>{

  const [show, setShow] = useState(false); //modal
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const [search, setSearch] = useState("")
  
return(
    <div className="container container  d-flex align-items-center flex-column mt-5">
        <p>Admin</p>
        
        <p>Lista de aeroportos com passagens disponíveis</p>
        <div className='m-2'>
        <Button variant="success" onClick={handleShow}>Criar novo trajeto</Button>
        </div>
         <Form>
          <InputGroup>
          <Form.Control className='m-3' onChange={(e) => setSearch(e.target.value)} placeholder="Busque o aeroporto" />
          </InputGroup>
         </Form>

        {/* <ReactBootStrap.Table></ReactBootStrap.Table> */}
        <ReactBootStrap.Table striped bordered hover >
      <thead>
        <tr>
          <th>id</th>
          <th>Partida</th>
          <th>Destino</th>
          <th>Dia</th>
          <th>Horario</th>
          <th>valor</th>
        </tr>
      </thead>
      <tbody>
        {voos.filter((voo)=>{
          return search.toLowerCase() ===''? voo: voo.partida.toLowerCase()
          .includes(search)
        })
        
        .map(renderVoos)}
     </tbody>
    </ReactBootStrap.Table>
       
    <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Trajeto</Modal.Title>
        </Modal.Header>
        <Modal.Body>

        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Partida</Form.Label>
        <Form.Control type="text" placeholder="Partida" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Destino</Form.Label>
        <Form.Control type="text" placeholder="Destino" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Dia</Form.Label>
        <Form.Control type="date" placeholder="Dia" />
        
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Horario</Form.Label>
        <Form.Control type="time" placeholder="Horario" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Valor</Form.Label>
        <Form.Control type="number" placeholder="Valor" />
      </Form.Group>

 
    </Form>

        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Fechar
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Salvar alterações
          </Button>
        </Modal.Footer>
      </Modal>
        
    </div>
)

}

export default AdminPassports