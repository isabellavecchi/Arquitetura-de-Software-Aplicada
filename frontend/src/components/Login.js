import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { Link, NavLink } from "react-router-dom";
import { useForm } from "react-hook-form";
import { login } from '../auth'
import {useNavigate} from 'react-router-dom'

const Login = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();

  const navigate=useNavigate()


  const loginUsuario=(data)=>{
    console.log(data)

    const requestOptions={
        method:"POST",
        headers:{
            'content-type':'application/json'
        },
        body:JSON.stringify(data)
    }
     
    fetch('/auth/login',requestOptions)
    .then(res=>res.json())
    .then(data=>{
        console.log(data.access_token)
        
        if (data){
         login(data.access_token)

         navigate('/adminV')
        }
        else{
            alert('Invalid username or password')
        }


    })



    reset()
 }
  return (
    <div className="container  d-flex align-items-center flex-column my-5">
      Login
      <div className="form">
        <Form>
          <Form.Group className="" controlId="login">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="text"
              placeholder="Preencha seu email"
              
              {...register("email", {
                required: true,
                pattern: /^\S+@\S+$/i,
                maxLength: 40,
              })}
            />
          </Form.Group>
          {errors.email && (
            <p style={{ color: "red" }}>
              <small>Preencha o campo de email corretamente</small>
            </p>
          )}
          {errors.email?.type === "maxLength" && (
            <p style={{ color: "red" }}>
              <small>Quantidade máxima de caracteres ultrapassada</small>
            </p>
          )}

          <br></br>
          <Form.Group className="" controlId="senha">
            <Form.Label>Senha</Form.Label>
            <Form.Control
              type="password"
              placeholder="Senha"
              {...register("senha", { required: true, minLength: 8 })}
            />
          </Form.Group>
          {errors.senha && (
            <p style={{ color: "red" }}>
              <small>Preencha o campo de senha corretamente</small>
            </p>
          )}

          {errors.senha?.type === "minLength" && (
            <p style={{ color: "red" }}>
              <small>Quantidade minima de caracteres é 8.</small>
            </p>
          )}
          <br></br>
          <div className="w-100">
            <Button
              onClick={handleSubmit(loginUsuario)}
              as="sub"
              className="align-items-center mb-2"
              variant="primary"
              type="submit"
            >
              Entrar
            </Button>
          </div>
          <small>
            <Link className="linkar" as={NavLink} to="/cadastro">
              Não tem conta? Cadastre-se aqui!
            </Link>
          </small>
        </Form>
      </div>
    </div>
  );
};

export default Login;
