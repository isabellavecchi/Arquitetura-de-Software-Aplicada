import React from 'react';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import { FaPen } from "react-icons/fa";
import {AiOutlineClose} from "react-icons/ai";
import {useState, useEffect} from 'react';
import axios from 'axios';
import * as ReactBootStrap from 'react-bootstrap';


const voos = [
  {partida:"uberlandia", destino:"sao paulo", dia:"22/07/2023", horario:"19:00", valor:"250,00"},
  {partida:"uberlandia", destino:"sao paulo", dia:"22/07/2023", horario:"19:00", valor:"250,00"},
  {partida:"uberlandia", destino:"sao paulo", dia:"22/07/2023", horario:"19:00", valor:"250,00"},
  {partida:"uberlandia", destino:"sao paulo", dia:"22/07/2023", horario:"19:00", valor:"250,00"}
]




const AdminPage=()=>{
  
  // const [colunas, setColunas] = useState(voos)
  const [posts, setPosts] = useState({ blogs: []})

  useEffect(() => {
    const fetchPostList = async() => {
      const {data} = await axios("https://jsonplaceholder.typicode.com/posts")
      setPosts({blogs: data})
      console.log(data)
    }  
      fetchPostList()


  }, [setPosts])
 
return(
    <div className="container container  d-flex align-items-center flex-column mt-5">
        <p>Admin</p>
        
        <p>Lista de aeroportos com passagens disponíveis</p>
        <div className='m-2'>
        <Button variant="success">Criar novo trajeto</Button>
        </div>

        <ReactBootStrap.Table striped bordered hover>
      <thead>
        <tr>
          <th>#</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Username</th>
          <th>Editar</th>
        </tr>
      </thead>
      <tbody>
        {
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
        }
        
      
      </tbody>
    </ReactBootStrap.Table>
       
        
    </div>
)

}

export default AdminPage