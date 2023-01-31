import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import Modal from 'react-bootstrap/Modal';
import { InputGroup } from 'react-bootstrap';
import * as ReactBootStrap from 'react-bootstrap';
import Form from 'react-bootstrap/Form';


export const voos = [
  {id:"1",partida:"uberlandia", destino:"sao paulo", diaP:"22/07/2023", horarioP:"19:00",diaC:"25/11/2023", horarioC:"19:00", valor:"250,00" ,passagens:"25"},
  {id:"2",partida:"sao paulo", destino:"uberlandia", diaP:"24/07/2023", horarioP:"10:00",diaC:"25/11/2023", horarioC:"19:00", valor:"340,00" ,passagens:"25"},
  {id:"3",partida:"belo horizonte", destino:"sao paulo", diaP:"20/07/2023", horarioP:"13:00",diaC:"25/11/2023", horarioC:"19:00", valor:"370,00" ,passagens:"25"},
  {id:"4",partida:"uberlandia", destino:"bahia", diaP:"21/07/2023", horarioP:"9:00",diaC:"25/11/2023",horarioC:"19:00", valor:"650,00" ,passagens:"25"}
]

export function renderVoos (voo, index) {
  const [lgShow, setLgShow] = useState(false);
  return(
    <>
      <tr key={index}>
      <td>{voo.id}</td>
      <td>{voo.partida}</td>
      <td>{voo.destino}</td>
      <td>{voo.diaP}</td>
      <td>{voo.horarioP}</td>
      <td>{voo.diaC}</td>
      <td>{voo.horarioC}</td>
      <td>{voo.valor}</td>
      <td>{voo.passagens}</td>
      <td className='d-flex flex-row'> 
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
            Editar passagem
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail" >
        <Form.Label>Partida Atual: ({(voo.partida)})</Form.Label>
        <Form.Control type="text" placeholder="novo local de partida"  />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Destino Atual: ({(voo.destino)})</Form.Label>
        <Form.Control type="text" placeholder="novo local de destino" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Dia de pardita atual: ({(voo.diaP)})</Form.Label>
        <Form.Control type="date" placeholder="Dia" />
        
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Horario de partida Atual: ({(voo.horarioP)})</Form.Label>
        <Form.Control type="time" placeholder="novo Horario de Partida" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Dia de chegada atual: ({(voo.diaC)})</Form.Label>
        <Form.Control type="date" placeholder="Dia" />
        
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Horario de chegada Atual: ({(voo.horarioC)})</Form.Label>
        <Form.Control type="time" placeholder="novo Horario de Chegada" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Passagens: ({(voo.passagens)})</Form.Label>
        <Form.Control type="number" placeholder="novo Horario de Chegada" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Valor da passagem atual: ({(voo.valor)})</Form.Label>
        <Form.Control type="number" placeholder="novo valor de passagem" />
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
        <ReactBootStrap.Table striped bordered hover  className='text-center'>
      <thead>
        <tr >
          <th>id</th>
          <th>Partida</th>
          <th>Destino</th>
          <th>Dia da Partida</th>
          <th>Horario de partida</th>
          <th>Dia da chegada</th>
          <th>Horario de chegada</th>
          <th>Valor</th>
          <th>Passagens disponíveis</th>
          <th>Editar</th>
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

export default AdminTickets