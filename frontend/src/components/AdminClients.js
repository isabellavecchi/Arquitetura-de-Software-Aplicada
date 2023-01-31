import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import Modal from 'react-bootstrap/Modal';
import { InputGroup } from 'react-bootstrap';
import * as ReactBootStrap from 'react-bootstrap';
import Form from 'react-bootstrap/Form';


export const clientss = [
  {id:"1",usuario:"Joao", email:"joao@mail.com", viagens:"São Paulo -> Uberlândia no dia 22/07/2023"},
  {id:"2",usuario:"Maria", email:"maria@bol.com", viagens:"Uberlândia -> São Paulo 24/07/2023"},
  {id:"3",usuario:"Isabella", email:"isabella@yahoo.com", viagens:"São Paulo -> Uberlândia 21/07/2023"},
  {id:"4",usuario:"Augusto", email:"augusto@hotmail.com", viagens:"São Paulo -> Uberlândia 21/07/2023"}
]

export function renderClientes (clients, index) {
  const [lgShow, setLgShow] = useState(false);
  
  return(
 
    
    <>
   
    
      <tr key={index}>
      <td>{clients.id}</td>
      <td>{clients.usuario}</td>
      <td>{clients.email}</td>
      <td>{clients.viagens}</td>
      <td> 
        <Button className='mx-1' variant="info" onClick={() => setLgShow(true)}><FaPen color="white" /></Button>
        <Button className='mx-1' variant="danger"><AiOutlineClose /> </Button>
        </td>
    </tr>
      <Modal
        size="lg"
        show={lgShow}
        onHide={() => setLgShow(false)}
        aria-labelledby="example-modal-sizes-title-lg"
      >
        <Modal.Header closeButton>
          <Modal.Title id="example-modal-sizes-title-lg">
            Large Modal
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail" >
        <Form.Label>Nome atual ({clients.usuario})</Form.Label>
        <Form.Control type="text" placeholder="novo nome de usuario"  />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Email atual ({(clients.email)})</Form.Label>
        <Form.Control type="text" placeholder="novo email para o usuario" />
      </Form.Group>

 
    </Form>
          <Modal.Footer>
          <Button variant="secondary" onClick={() => setLgShow(false)} >
            Cancelar
          </Button>
          <Button variant="primary" >
            Salvar alterações
          </Button>
        </Modal.Footer>
      

        </Modal.Body>
      </Modal>

      </>



)

}


const AdminTickets=()=>{

  const [show, setShow] = useState(false); //modal
  const handleClose = () => setShow(false);




  const [search, setSearch] = useState("")
  
return(
    <div className="container container  d-flex align-items-center flex-column mt-5">
        <p>Admin</p>
        
        <p>Lista de usuarios</p>

         <Form>
          <InputGroup>
          <Form.Control className='m-3' onChange={(e) => setSearch(e.target.value)} placeholder="Busque o aeroporto" />
          </InputGroup>
         </Form>

        {/* <ReactBootStrap.Table></ReactBootStrap.Table> */}
        <ReactBootStrap.Table striped bordered hover className="text-center">
      <thead>
        <tr>
          <th>id</th>
          <th>Cliente</th>
          <th>Email</th>
          <th>Viagens</th>
          <th>Editar</th>
        </tr>
      </thead>
      <tbody>
        {clientss.filter((clients)=>{
          return search.toLowerCase() ===''? clients: clients.usuario.toLowerCase()
          .includes(search)
        })
        
        .map(renderClientes)}
     </tbody>
    </ReactBootStrap.Table>
       
    <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Trajeto</Modal.Title>
        </Modal.Header>
        <Modal.Body>

        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>cliente</Form.Label>
        <Form.Control type="text" placeholder="cliente" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>email</Form.Label>
        <Form.Control type="text" placeholder="email" />
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

export default AdminTickets