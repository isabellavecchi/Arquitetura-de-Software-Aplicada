import React from 'react'
import { Link, NavLink } from 'react-router-dom'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const Cadastro=()=>{
return(
    <div className="container  d-flex align-items-center flex-column mt-5">
        Cadastro
        <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Usuario</Form.Label>
        <Form.Control type="text" placeholder="Entre com seu usuario" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email</Form.Label>
        <Form.Control type="email" placeholder="Entre com seu email" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Senha</Form.Label>
        <Form.Control type="password" placeholder="Senha" />
      </Form.Group>

       <Button as={NavLink} to="/login" className='align-items-center' variant="primary" type="submit">
        Entrar
      </Button>
        <p>
        <Link className='linkar' as={NavLink} to="/login">Já possui conta? Entre aqui!</Link>
        </p> 
        </Form>
        
    </div>
)

}

export default Cadastro