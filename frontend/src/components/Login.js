import React from 'react'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Link,NavLink } from 'react-router-dom';

const Login=()=>{
return(
    <div className="container  d-flex align-items-center flex-column mt-5">
        <p>Login</p>
         
        
        <Form>
      <Form.Group className="mb-3" controlId="email">
        <Form.Label>Usuario</Form.Label>
        <Form.Control type="text" placeholder="Entre com seu email" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="senha">
        <Form.Label>Senha</Form.Label>
        <Form.Control type="password" placeholder="Senha" />
      </Form.Group>
       <Button as={NavLink} to="/login" className='align-items-center' variant="primary" type="submit">
        Entrar
      </Button>
        <p>
        <Link className='linkar' as={NavLink} to="/cadastro">Não tem conta? Cadastre-se aqui!</Link>
        </p> 
        </Form>
        
    </div>
)

}

export default Login