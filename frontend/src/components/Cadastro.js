import React, { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useForm } from "react-hook-form";
import { Alert } from "react-bootstrap";

// login email senha

const Cadastro = () => {

  const [show, setShow] = useState(false);
  const [serverResponse,setServerResponse]=useState('')
  const {register,reset,handleSubmit,formState: { errors },} = useForm();

  const submitForm = (data) => {
    if (data.password === data.confirmPassword) {
      console.log(data);

      const body = {
        usuario: data.usuario,
        email: data.email,
        senha: data.senha,
      };
      const requestOptions = {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(body),
      };
      fetch("/cadastro", requestOptions)
        .then((res) => res.json())
        .then((data) =>{
          console.log(data)
          console.log(serverResponse)
          setServerResponse(data.message)
          setShow(true)
      }
        )
        .catch((err) => console.log(err));

      reset();
    } else {
      alert("Senhas não combinam");
    }
  };
  // console.log(watch("usuario"));

  return (
    <div className="container  d-flex align-items-center flex-column my-5">
      
      {show? 
      <>
      <Alert variant="success" onClose={() => setShow(false)} dismissible>
      <p>{serverResponse}</p>
      </Alert>
      </>  : Cadastro
       }
      <div className="form">
        <Form>
          <Form.Group className="m-1" controlId="login">
            <Form.Label>Usuario</Form.Label>
            <Form.Control
              type="text"
              placeholder="Preencha seu nome"
              {...register("usuario", { required: true, maxLength: 25 })}
            />
            {/* tem que ser igual a variavel do models */}
            {errors.usuario && (
              <p style={{ color: "red" }}>
                <small>Preencha o campo de Usuário</small>
              </p>
            )}
            {errors.usuario?.type === "maxLength" && (
              <p style={{ color: "red" }}>
                <small>Quantidade máxima de caracteres ultrapassada</small>
              </p>
            )}
          </Form.Group>

          <Form.Group className="m-1" controlId="email">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              placeholder="Entre com seu email"
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

          <Form.Group className="m-1" controlId="senha">
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
          <Form.Group className="m-1" controlId="confirmSenha">
            <Form.Label>Confime sua Senha</Form.Label>
            <Form.Control
              type="password"
              placeholder="Confirme sua Senha"
              {...register("confirmSenha", { required: true, minLength: 8 })}
            />
          </Form.Group>

          {errors.confirmSenha && (
            <p style={{ color: "red" }}>
              <small>Preencha o campo de confirmação de senha</small>
            </p>
          )}

          {errors.confirmSenha?.type === "minLength" && (
            <p style={{ color: "red" }}>
              <small>Quantidade minima de caracteres é 8.</small>
            </p>
          )}
          <div className="w-100">
            <Button
              onClick={handleSubmit(submitForm)}
              as="sub"
              className="align-items-center mb-2"
              variant="primary"
              type="submit"
            >
              Cadastrar
            </Button>
          </div>

          <small>
            <Link className="linkar" as={NavLink} to="/login">
              Já possui conta? Entre aqui!
            </Link>
          </small>
        </Form>
      </div>
    </div>
  );
};

export default Cadastro;
