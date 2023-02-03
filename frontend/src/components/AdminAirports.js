import React, { useState,useEffect } from 'react';
import Button from 'react-bootstrap/Button';
// import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import Modal from 'react-bootstrap/Modal';
import { InputGroup } from 'react-bootstrap';
import * as ReactBootStrap from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import { useForm } from 'react-hook-form';


export const aeroportos = [
  {id:"1",nomeAeroporto:"congonhas",cidade:"uberlandia", estado:"MG"},
  {id:"2",nomeAeroporto:"jaci de assis",cidade:"rio de janeiro", estado:"RJ"},
  {id:"3",nomeAeroporto:"getulio vargas",cidade:"Pirapora", estado:"MG"},
  {id:"4",nomeAeroporto:"santos drumond",cidade:"sao paulo", estado:"SP"}
]

export const RenderAeroportos = (aeroporto, index) => {
  // const [lgShow, setLgShow] = useState(false);
  const {handleSubmit}=useForm()
 
  const deletaAeroporto=(data)=>{
    console.log(aeroporto.id)
    let token=localStorage.getItem('REACT_TOKEN_AUTH_KEY')

    const requestOptions={
        method:'DELETE',
        headers:{
            'content-type':'application/json',
            'Authorization':`Bearer ${JSON.parse(token)}`
        }
    }


    fetch(`/aeroportos/deletar/${aeroporto.id}`,requestOptions)
    .then(res=>res.json())
    .then(data=>{
        console.log(data) 
    
    })
    .catch(err=>console.log(err))
}
  
  
  
  
  
  return(
    <>
      <tr key={index}>
      <td>{aeroporto.id}</td>
      <td>{aeroporto.nomeAeroporto}</td>
      <td>{aeroporto.cidade}</td>
      <td>{aeroporto.estado}</td>
      <td> 
        {/* <Button className='mx-1' variant="info" onClick={() => setLgShow(true)}><FaPen color="white" /></Button> */}
        <Button onClick={handleSubmit(deletaAeroporto)} className='mx-1' variant="danger"><AiOutlineClose /> </Button>
        </td>
    </tr>
    
    {/* modal de update */}
    
    {/* <Modal
        size="lg"
        // show={lgShow}
        // onHide={() => setLgShow(false)}
        aria-labelledby="example-modal-sizes-title-lg"
      >
        <Modal.Header closeButton>
          <Modal.Title id="example-modal-sizes-title-lg">
            Editar valores
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <Form>
     
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Estação atual ({(aeroporto.estacao)})</Form.Label>
        <Form.Control type="text" placeholder="nova localização de estação" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Quantidade de avioes atual: {aeroporto.avioes}</Form.Label>
        <Form.Control type="text" placeholder="nova quantidade de aviões" />
        
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
    */}

</>
  )
}


const AdminAirports=()=>{

  const [show, setShow] = useState(false); //modal
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const [search, setSearch] = useState("")

//Get dos valores da tabela 
//   const [aeroportos, setAeroportos] = useState([]);
//   useEffect(
//     () => {
//         fetch('/aeroportos')
//             .then(res => res.json())
//             .then(data => {setAeroportos(data)})
//             .then(data=>console.log(data))
//             .catch(err => console.log(err))
//     }, []
// );

const {register, handleSubmit}=useForm()

const criaAerporto=(data)=>{
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
  fetch('/aeroportos', requestOptions)
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
        
        <p>Lista de aeroportos</p>
        <div className='m-2'>
        <Button variant="success" onClick={handleShow}>Criar novo aeroporto</Button>
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
          <th>Nome do aeroporto</th>
          <th>Cidade</th>
          <th>Estado</th>
          <th>Excluir aeroporto</th>
        </tr>
      </thead>
      <tbody>
        
        {aeroportos.filter((aeroporto)=>{
          return search.toLowerCase() ===''? aeroporto: aeroporto.nomeAeroporto.toLowerCase()
          .includes(search)
          
        })
        
        .map(RenderAeroportos)}
     </tbody>
    </ReactBootStrap.Table>
       
    <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Aeroporto</Modal.Title>
        </Modal.Header>
        <Modal.Body>

        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Nome do Aeroporto</Form.Label>
        <Form.Control type="text" placeholder="nome do Aeroporto" {...register('nomeAeroporto',{required:true})}/>
      </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Cidade</Form.Label>
        <Form.Control type="text" placeholder="cidade" {...register('cidade',{required:true})}/>
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Estado</Form.Label>
        <Form.Control type="text" placeholder="estado" {...register('estado',{required:true})}/>
      </Form.Group>

  


 
    </Form>

        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Fechar
          </Button>
          <Button variant="primary" onClick={handleSubmit(criaAerporto)}>
            Salvar alterações
          </Button>
        </Modal.Footer>
      </Modal>
        
    </div>
)

}

export default AdminAirports