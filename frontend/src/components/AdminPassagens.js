import React, { useState, useEffect} from 'react';
import Button from 'react-bootstrap/Button';
// import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import Modal from 'react-bootstrap/Modal';
import { InputGroup } from 'react-bootstrap';
import * as ReactBootStrap from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import { useForm } from 'react-hook-form';
import { voos } from './AdminVoos';


//mudar o nome de passagenss para passagens
export const passagens = [
  //voos.json =  {id:"1",partida:"uberlandia", destino:"sao paulo", diaPartida:"22/07/2023", horarioPartida:"19:00",diaChegada:"25/11/2023", horarioChegada:"19:00", valor:"250,00"}
  //mas não será incluso a quantidade de passagens no json
  //{id:"1",nomePassageiro:"Joao", cpf:"1111111111", viagem:{voos.json}},
  {id:"1",nomePassageiro:"Joao", cpf:"111111111", viagem:"Uberlândia -> São Paulo 24/07/2023"},
  {id:"2",nomePassageiro:"Maria", cpf:"maria@bol.com", viagem:"Uberlândia -> São Paulo 24/07/2023"},
  {id:"3",nomePassageiro:"Isabella", cpf:"isabella@yahoo.com", viagem:"São Paulo -> Uberlândia 21/07/2023"},
  {id:"4",nomePassageiro:"Augusto", cpf:"augusto@hotmail.com", viagem:"São Paulo -> Uberlândia 21/07/2023"}
]


export const RenderVoosSelect = (voo, index) => {
  return(
  
  <option value={voo.id}>De {voo.partida} à {voo.destino} no dia: {voo.dia} as {voo.horario} por {voo.valor}   </option>
  )
}



export const RenderPassagens = (Passagens, index) => {
  
  // const [lgShow, setLgShow] = useState(false);
  return(
   <>
   
    
      <tr key={index}>
      <td>{Passagens.id}</td>
      <td>{Passagens.nomePassageiro}</td>
      <td>{Passagens.cpf}</td>
      <td>{Passagens.viagem}</td>
      <td> 
        {/* <Button className='mx-1' variant="info" onClick={() => setLgShow(true)}><FaPen color="white" /></Button> */}
        <Button className='mx-1' variant="danger"><AiOutlineClose /> </Button>
        </td>
    </tr>
      <Modal
        size="lg"
        // show={lgShow}
        // onHide={() => setLgShow(false)}
        aria-labelledby="example-modal-sizes-title-lg"
      >
        <Modal.Header closeButton>
          <Modal.Title id="example-modal-sizes-title-lg">
            Large Modal
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <Form>
      <Form.Group className="mb-3" controlId="formBasiccpf" >
        <Form.Label>Nome atual ({Passagens.nomePassageiro})</Form.Label>
        <Form.Control type="text" placeholder="novo nome de nomePassageiro"  />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>cpf atual ({(Passagens.cpf)})</Form.Label>
        <Form.Control type="text" placeholder="novo cpf para o nomePassageiro" />
      </Form.Group>

 
    </Form>
          <Modal.Footer>
          {/* <Button variant="secondary" onClick={() => setLgShow(false)} >
            Cancelar
          </Button> */}
          <Button variant="primary" >
            Salvar alterações
          </Button>
        </Modal.Footer>
      

        </Modal.Body>
      </Modal>

      </>



)

}


const AdminPassagens=()=>{
  const [search, setSearch] = useState("");
  const [show, setShow] = useState(false); //modal
  
  const [show2, setShow2] = useState(false);//modal2
  const handleClose2 = () => setShow2(false);
  const handleShow2 = () => setShow2(true);

  const handleClose = () => setShow(false);


  //Get dos valores da tabela 
//   const [passagens, setPassagens] = useState([]);
//   useEffect(
//     () => {
//         fetch('/passagens')
//             .then(res => res.json())
//             .then(data => {setPassagens(data)})
//             .then(data=>console.log(data))
//             .catch(err => console.log(err))
//     }, []
// );

  



const {register, handleSubmit,formState:{errors}}=useForm()
const vendePassagem=(data)=>{
  //metodo POST para comprar passagem mandar id do voo cpf e nome do passageiro id do voo= passagem
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
    fetch('/passagem', requestOptions)
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
  
        
    })
    .catch(err=>console.log(err))
    // handleClose()
   
  }
  
  
return(
    <div className="container container  d-flex align-items-center flex-column mt-5">
        <p>Admin</p>
        
        <p>Lista de passagens por nome do Passageiro</p>
        <Button className='m-1' variant="primary" onClick={handleShow2}>Vender Passagem</Button>
         <Form>
          <InputGroup>
          <Form.Control className='m-3' onChange={(e) => setSearch(e.target.value)} placeholder="Busque o aeroporto" />
            
          </InputGroup>
         </Form>

       
        <ReactBootStrap.Table striped bordered hover className="text-center">
      <thead>
        <tr>
          <th>id</th>
          <th>Cliente</th>
          <th>cpf</th>
          <th>viagem</th>
          <th>Editar</th>
        </tr>
      </thead>
      <tbody>
        {passagens.filter((Passagens)=>{
          return search.toLowerCase() ===''? Passagens: Passagens.nomePassageiro.toLowerCase()
          .includes(search)
        })
        
        .map(RenderPassagens)}
     </tbody>
    </ReactBootStrap.Table>
       
    <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Trajeto</Modal.Title>
        </Modal.Header>
        <Modal.Body>

        <Form>
      <Form.Group className="mb-3" controlId="formBasiccpf">
        <Form.Label>cliente</Form.Label>
        <Form.Control type="text" placeholder="cliente" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>cpf</Form.Label>
        <Form.Control type="text" placeholder="cpf" />
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
        



{/* modal de venda de passagem POST */}
<Modal show={show2} onHide={handleClose2}>
        <Modal.Header closeButton>
          <Modal.Title>Novo Voo</Modal.Title>
        </Modal.Header>
        <Modal.Body>

        <Form>
      <Form.Group className="mb-3" controlId="passagem">
      <Form.Label>Partida</Form.Label>
      <Form.Select aria-label="Default select example" {...register('viagem',{required:true})}>
       <option>Aeroportos disponiveis</option>
       {voos.map(RenderVoosSelect)}
       </Form.Select>
      </Form.Group>

      <Form.Group className="mb-3" controlId="nomePassageiro">
        <Form.Label>Nome do passageiro</Form.Label>
        <Form.Control type="text" placeholder="nome do passageiro" {...register('nomePassageiro',{required:true})}/>
      </Form.Group>

      <Form.Group className="mb-3" controlId="cpf">
        <Form.Label>Cpf </Form.Label>
        <Form.Control type="text" placeholder="Cpf" {...register('cpf',{required:true})}/>
      </Form.Group>

 
    </Form>

        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Fechar
          </Button>
          <Button variant="primary" onClick={handleSubmit(vendePassagem)}>
            Salvar alterações
          </Button>
        </Modal.Footer>
      </Modal>







    </div>

)

}

export default AdminPassagens