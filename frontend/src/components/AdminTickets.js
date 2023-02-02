import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import Modal from 'react-bootstrap/Modal';
import { InputGroup } from 'react-bootstrap';
import * as ReactBootStrap from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import { aeroportos } from './AdminAirports';
import { passagens } from './AdminPassagens';

export const voos = [
  {id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00" ,passagens:"25"},
  {id:"2",partida:"sao paulo", destino:"uberlandia", diaPartida:"24/07/2023", horarioPartida:"10:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"340,00" ,passagens:"25"},
  {id:"3",partida:"belo horizonte", destino:"sao paulo", diaPartida:"20/07/2023", horarioPartida:"13:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"370,00" ,passagens:"25"},
  {id:"4",partida:"uberlandia", destino:"bahia", diaPartida:"21/07/2023", horarioPartida:"9:00",diaChegada:"25/11/2023",horarioChegada:"19:00", valor:"650,00" ,passagens:"25"}
]

<<<<<<< Updated upstream
// function handleClick() {
    
//   // Send data to the backend via POST
//   fetch('/voos', {  // Enter your IP address here

//     method: 'POST', 
//     mode: 'cors', 
//     body: JSON.stringify(voos), // body data type must match "Content-Type" header
//     headers: {
//       'Content-Type': 'application/json'
//     },
//   })
  
// }



 export const RenderAeroportosSelect = (aeroporto, index) => {
   return(
      <option value={aeroporto.id}> Aeroporto : {aeroporto.nomeAeroporto} em {aeroporto.cidade} - {aeroporto.estado}   </option>
      )

 }
  export const RenderVoosSelect = (voo, index) => {
   return(
   
   <option value={voo.id}>De {voo.partida} à {voo.destino} no dia: {voo.dia} as {voo.horario} por {voo.valor}   </option>
    
   

   )

 }



const AdminTickets=()=>{

  const [show3, setShow3] = useState(false); //modal
  const handleClose3 = () => setShow3(false);
  const handleShow3 = () => setShow3(true);
 const RenderVoos = (voo, index) => {

=======

export const RenderVoos = (voo, index) =>{
  const [lgShow, setLgShow] = useState(false);
>>>>>>> Stashed changes
  return(
    <>
      <tr key={index}>
      <td>{voo.id}</td>
      <td>{voo.partida}</td>
      <td>{voo.destino}</td>
      <td>{voo.diaPartida}</td>
      <td>{voo.horarioPartida}</td>
      <td>{voo.diaChegada}</td>
      <td>{voo.horarioChegada}</td>
      <td>{voo.valor}</td>
      <td>{voo.passagens}</td>
      <td className='d-flex flex-row'> 
        <Button className='mx-1' variant="info" onClick={handleShow3}><FaPen color="white" /></Button>
        <Button className='mx-1' variant="danger"><AiOutlineClose /> </Button>
      </td>
    </tr>
    <Modal show={show3} onHide={handleClose3}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Voo</Modal.Title>
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
        <Form.Label>Dia de pardita atual: ({(voo.diaPartida)})</Form.Label>
        <Form.Control type="date" placeholder="Dia" />
        
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Horario de partida Atual: ({(voo.horarioPartida)})</Form.Label>
        <Form.Control type="time" placeholder="novo Horario de Partida" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Dia de chegada atual: ({(voo.diaChegada)})</Form.Label>
        <Form.Control type="date" placeholder="Dia" />
        
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Horario de chegada Atual: ({(voo.horarioChegada)})</Form.Label>
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
          <Button variant="secondary"  onClick={handleClose3} >
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

  const [show, setShow] = useState(false); //modal
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const [show2, setShow2] = useState(false);//modal2
  const handleClose2 = () => setShow2(false);
  const handleShow2 = () => setShow2(true);

  const [search, setSearch] = useState("");


  // const [voos, setvoos] = useState({
  //   id:0,
  //   partida: "",
  //   destino: "",
  //   diaPartida: "",
  //   horarioPartida:"",
  //   diaChegada:"",
  //   horarioChegada:"",
  //   valor:"",
  //   passagens:"",
   
  // });
  
  // useEffect(() => {
  //   // Usando fetch para pegar os dados do endpoint do flask
  //   fetch("/voos").then((res) =>
  //       res.json().then((voos) => {
  //           // seta os valores da api
  //           setvoos({
  //               id: voos.id,
  //               partida: voos.partida,
  //               destino: voos.destino,
  //               diaPartida: voos.diaPartida,
  //               horarioPartida: voos.horarioPartida,
  //               diaChegada: voos.diaChegada,
  //               horarioChegada: voos.horarioChegada,
  //               valor: voos.valor,
  //               passagens: voos.passagens
  //           });
  //       })
  //   );
  // }, []);
  

  
return(







    <div className="container container  d-flex align-items-center flex-column mt-5">
        <p>Admin</p>
        
        <p>Lista de aeroportos com passagens disponíveis</p>
        <div className='m-2'>
        <Button className='m-1' variant="success" onClick={handleShow}>Criar novo voo</Button>
        <Button className='m-1' variant="primary" onClick={handleShow2}>Vender Passagem</Button>
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
        
        .map(RenderVoos)}
     </tbody>
    </ReactBootStrap.Table>
       
    <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Voo</Modal.Title>
        </Modal.Header>
        <Modal.Body>

        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
      <Form.Label>Partida</Form.Label>
      <Form.Select aria-label="Default select example">
       <option>Aeroportos disponiveis</option>
       {aeroportos.map(RenderAeroportosSelect)}
       </Form.Select>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
      <Form.Label>Destino</Form.Label>
      <Form.Select aria-label="Default select example">
       <option>Aeroportos disponiveis</option>
       {aeroportos.map(RenderAeroportosSelect)}
       </Form.Select>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Dia da Partida</Form.Label>
        <Form.Control type="date" placeholder="Dia da Partida" />
        
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Horario da Partida</Form.Label>
        <Form.Control type="time" placeholder="Horario da Partida" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Dia da Chegada</Form.Label>
        <Form.Control type="date" placeholder="Dia da Chegada" />
        
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Horario da Chegada</Form.Label>
        <Form.Control type="time" placeholder="Horario da Chegada" />
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


      {/* modal de venda de passagem */}
      <Modal show={show2} onHide={handleClose2}>
         <Modal.Header closeButton>
           <Modal.Title>Comprar passagem</Modal.Title>
         </Modal.Header>
         <Modal.Body>Selecione qual passagem deseja comprar
         <Form.Select aria-label="Default select example">/       <option>Vôos disponiveis</option>
       {voos.map(RenderVoosSelect)}
        </Form.Select>

        <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Nome do passageiro</Form.Label>
        <Form.Control type="text" placeholder="cliente" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Cpf</Form.Label>
        <Form.Control type="text" placeholder="email" />
      </Form.Group>

         </Modal.Body>
         <Modal.Footer>
           <Button variant="primary" >
             Vender passagem
           </Button>
         </Modal.Footer>
      </Modal>
   
        
    </div>
)

}

export default AdminTickets