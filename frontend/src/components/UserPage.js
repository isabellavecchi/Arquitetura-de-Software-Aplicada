// import React, { useState } from 'react';
// import Button from 'react-bootstrap/Button';


// import Modal from 'react-bootstrap/Modal';
// // import { InputGroup } from 'react-bootstrap';
// import * as ReactBootStrap from 'react-bootstrap';
// import Form from 'react-bootstrap/Form';
// import {NavLink } from 'react-router-dom';
// import { voos } from './AdminTickets';

<<<<<<< Updated upstream
// export function RenderVoos (voo, index) {
=======
// export function rendervoos (voo, index) {
>>>>>>> Stashed changes
//   const [lgShow, setLgShow] = useState(false);
//   return(
//     <>
//       <tr key={index}>
//       <td>{voo.id}</td>
//       <td>{voo.partida}</td>
//       <td>{voo.destino}</td>
//       <td>{voo.diaP}</td>
//       <td>{voo.horarioP}</td>
//       <td>{voo.diaC}</td>
//       <td>{voo.horarioC}</td>
//       <td>{voo.valor}</td>
//       <td> 
//         <Button variant="danger"> Cancelar Passagem </Button>
//         </td>
//     </tr>
//     <Modal
//         size="lg"
//         show={lgShow}
//         onHide={() => setLgShow(false)}
//         aria-labelledby="example-modal-sizes-title-lg"
//       >
//         <Modal.Header closeButton>
//           <Modal.Title id="example-modal-sizes-title-lg">
//             Editar valores
//           </Modal.Title>
//         </Modal.Header>
//         <Modal.Body>
//         <Form>
     
//       <Form.Group className="mb-3" controlId="formBasicPassword">
//         <Form.Label>Estação atual ({(voo.partida)})</Form.Label>
//         <Form.Control type="text" placeholder="nova localização de estação" />
//       </Form.Group>

//       <Form.Group className="mb-3" controlId="formBasicPassword">
//         <Form.Label>Quantidade de avioes atual: {voo.chegada}</Form.Label>
//         <Form.Control type="text" placeholder="nova quantidade de aviões" />
        
//       </Form.Group>


 
//     </Form>
//           <Modal.Footer>
//           <Button variant="secondary" onClick={() => setLgShow(false)} >
//             Cancelar
//           </Button>
//           <Button variant="primary" >
//             Salvar alterações
//           </Button>
//         </Modal.Footer>
      

//         </Modal.Body>
//       </Modal>

// </>
//   )
// }


// const UserPage=()=>{

//   const [show, setShow] = useState(false); //modal
//   const handleClose = () => setShow(false);
// //   const handleShow = () => setShow(true);

//   const [search] = useState("")
  
// return(
//     <div className="container container  d-flex align-items-center flex-column mt-5">
//         <p>Bem vindo usuario!</p>
//         <p>Minhas viagens</p>
//         <div className='m-2'>
//         <Button variant="success" as={NavLink} to="/passagens">Comprar nova passagem</Button>
//         </div>
   

//         {/* <ReactBootStrap.Table></ReactBootStrap.Table> */}
//         <ReactBootStrap.Table striped bordered hover className='text-center'>
//       <thead>
//         <tr>
//           <th>id</th>
//           <th>Partida</th>
//           <th>Destino</th>
//           <th>Dia de Partida</th>
//           <th>Horario de partida</th>
//           <th>Dia de chegada</th>
//           <th>Horario de chegada</th>
//           <th>Valor</th>
//         </tr>
//       </thead>
//       <tbody>
//         {voos.filter((voo)=>{
//           return search.toLowerCase() ===''? voo: voo.estacao.toLowerCase()
//           .includes(search)
//         })
        
<<<<<<< Updated upstream
//         .map(RenderVoos)}
=======
//         .map(rendervoos)}
>>>>>>> Stashed changes
//      </tbody>
//     </ReactBootStrap.Table>
       
//     <Modal show={show} onHide={handleClose}>
//         <Modal.Header closeButton>
//           <Modal.Title>Novo Trajeto</Modal.Title>
//         </Modal.Header>
//         <Modal.Body>

//         <Form>
//       <Form.Group className="mb-3" controlId="formBasicEmail">
//         <Form.Label>Estação</Form.Label>
//         <Form.Control type="text" placeholder="estacao" />
//       </Form.Group>

//       <Form.Group className="mb-3" controlId="formBasicPassword">
//         <Form.Label>Quantidade de aviões disponíveis</Form.Label>
//         <Form.Control type="text" placeholder="avioes" />
//       </Form.Group>


 
//     </Form>

//         </Modal.Body>
//         <Modal.Footer>
//           <Button variant="secondary" onClick={handleClose}>
//             Fechar
//           </Button>
//           <Button variant="primary" onClick={handleClose}>
//             Salvar alterações
//           </Button>
//         </Modal.Footer>
//       </Modal>
        
//     </div>
// )

// }

// export default UserPage