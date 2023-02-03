import React, { useState, useEffect} from 'react';
import Button from 'react-bootstrap/Button';
import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import Modal from 'react-bootstrap/Modal';
import { InputGroup } from 'react-bootstrap';
import * as ReactBootStrap from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import { aeroportos } from './AdminAirports';
import { useForm } from 'react-hook-form';





export const voos = [
  {id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00" ,passagens:"25"},
  {id:"2",partida:"sao paulo", destino:"uberlandia", diaPartida:"24/07/2023", horarioPartida:"10:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"340,00" ,passagens:"25"},
  {id:"3",partida:"belo horizonte", destino:"sao paulo", diaPartida:"20/07/2023", horarioPartida:"13:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"370,00" ,passagens:"25"},
  {id:"4",partida:"uberlandia", destino:"bahia", diaPartida:"21/07/2023", horarioPartida:"9:00",diaChegada:"25/11/2023",horarioChegada:"19:00", valor:"650,00" ,passagens:"25"}
]

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



const AdminVoos=()=>{

  const [show3, setShow3] = useState(false); //modal
  const handleClose3 = () => setShow3(false);
  const handleShow3 = () => setShow3(true);
 
  
  const RenderVoos = (voo, index) => {

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



  const [search, setSearch] = useState(""); //pesquisa
  
//Get dos valores da tabela 
//   const [voos, setVoos] = useState([]);
//   useEffect(
//     () => {
//         fetch('/voos')
//             .then(res => res.json())
//             .then(data => {setVoos(data)})
//             .then(data=>console.log(data))
//             .catch(err => console.log(err))
//     }, []
// );

const {register, handleSubmit,formState:{errors}}=useForm()

const criaVoo=(data)=>{
//metodo POST para enviar um voo  
  const token=localStorage.getItem('REACT_TOKEN_AUTH_KEY');
  console.log(data)

  const requestOptions={
    method:'POST',
    headers:{
      'content-type':'application/json',
      'Authorization':`Bearer ${JSON.parse(token)}`
    },
    body:JSON.stringify(data)

  }
  fetch('/voos', requestOptions)
  .then(res=>res.json())
  .then(data=>{
      console.log(data)

      const reload =window.location.reload()
      reload() 
  })
  .catch(err=>console.log(err))
  // handleClose()
 
}

  
return(


    <div className="container container  d-flex align-items-center flex-column mt-5">
        <p>Admin</p>
        
        <p>Lista de aeroportos com passagens disponíveis</p>
        <div className='m-2'>
        <Button className='m-1' variant="success" onClick={handleShow}>Criar novo voo</Button>
        
        </div>
         <Form>
          <InputGroup>
          <Form.Control className='m-3' onChange={(e) => setSearch(e.target.value)} placeholder="Busque o aeroporto" />
          </InputGroup>
         </Form>

{/* Tabela com a lista de voos */}
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

{/*Modal para criar novo voo POST */}
    <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Voo</Modal.Title>
        </Modal.Header>
        <Modal.Body>

        <Form>
      <Form.Group className="mb-3" controlId="partida">
      <Form.Label>Partida</Form.Label>
      <Form.Select aria-label="Default select example" {...register('partida',{required:true})}>
       <option>Aeroportos disponiveis</option>
       {aeroportos.map(RenderAeroportosSelect)}
       </Form.Select>
      </Form.Group>

      <Form.Group className="mb-3" controlId="destino">
      <Form.Label>Destino</Form.Label>
      <Form.Select aria-label="Default select example"  {...register('destino',{required:true})}>
       <option>Aeroportos disponiveis</option>
       {aeroportos.map(RenderAeroportosSelect)}
       </Form.Select>
      </Form.Group>

      <Form.Group className="mb-3" controlId="diaPartida">
        <Form.Label>Dia da Partida</Form.Label>
        <Form.Control type="date" placeholder="Dia da Partida"  {...register('diaPartida',{required:true})} />
        
      </Form.Group>

      <Form.Group className="mb-3" controlId="horarioPartida">
        <Form.Label>Horario da Partida</Form.Label>
        <Form.Control type="time" placeholder="Horario da Partida"  {...register('horarioPartida',{required:true})}/>
      </Form.Group>
      <Form.Group className="mb-3" controlId="diaChegada">
        <Form.Label>Dia da Chegada</Form.Label>
        <Form.Control type="date" placeholder="Dia da Chegada"  {...register('diaChegada',{required:true})} />
        
      </Form.Group>

      <Form.Group className="mb-3" controlId="horarioChegada">
        <Form.Label>Horario da Chegada</Form.Label>
        <Form.Control type="time" placeholder="Horario da Chegada"  {...register('horarioChegada',{required:true})} />
      </Form.Group>

      <Form.Group className="mb-3" controlId="valor">
        <Form.Label>Valor</Form.Label>
        <Form.Control type="number" placeholder="Valor" {...register('valor',{required:true})}/>
      </Form.Group>

 
    </Form>

        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Fechar
          </Button>
          <Button variant="primary" onClick={handleSubmit(criaVoo)}>
            Salvar alterações
          </Button>
        </Modal.Footer>
      </Modal>








        
    </div>
)

}

export default AdminVoos