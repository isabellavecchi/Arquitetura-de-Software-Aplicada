import React from "react";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
// import NavDropdown from 'react-bootstrap/NavDropdown';
import { NavLink } from "react-router-dom";
import { useAuth, logout } from "../auth";


const LoggedOutLinks = () => {
  return (
      <>
          <Navbar bg="light" expand="lg">
    <Container>
      <Navbar.Brand as={NavLink} to='/'>AviaTur</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link as={NavLink} to="/"> Home</Nav.Link>
          <Nav.Link as={NavLink} to="/login">Login</Nav.Link>
          <Nav.Link as={NavLink} to="/cadastro">Cadastrar</Nav.Link>
          {/* <Nav.Link as={NavLink} to="/passagens">Comprar passagens</Nav.Link> */}
          {/* <Nav.Link as={NavLink} to="/userP">Minhas viagens</Nav.Link> */}
        </Nav>
      </Navbar.Collapse>
    </Container>
  </Navbar>
      </>
  )
}
const LoggedInLinks = () => {
  return (
      <> <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand as={NavLink} to='/'>AviaTur</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            {/* <Nav.Link as={NavLink} to="/passagens">Comprar passagens</Nav.Link> */}
            {/* <Nav.Link as={NavLink} to="/userP">Minhas viagens</Nav.Link> */}
            <Nav.Link as={NavLink} to="/"> Home</Nav.Link>
            <Nav.Link as={NavLink} to="/adminT">Administrar Voos</Nav.Link>
            <Nav.Link as={NavLink} to="/adminC">Administrar Passagens</Nav.Link>
            <Nav.Link as={NavLink} to="/adminA">Administrar Aeroportos</Nav.Link>
            <Nav.Link onClick={()=>{logout()}}>Logout</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
      </>
  )
}

const Menu = ()=>{

      const [logged]=useAuth();

    return(
      <div>
      {logged?<LoggedInLinks/>:<LoggedOutLinks/>}
      </div>
    )
}



export default Menu