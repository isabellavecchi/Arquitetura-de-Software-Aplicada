import React from "react";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
// import NavDropdown from 'react-bootstrap/NavDropdown';
import { NavLink } from "react-router-dom";

const Menu = ()=>{

    return(
        <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand as={NavLink} to='/'>AviaTur</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={NavLink} to="/"> Home</Nav.Link>
            <Nav.Link as={NavLink} to="/cadastro">Cadastrar</Nav.Link>
            <Nav.Link as={NavLink} to="/login">Login</Nav.Link>
            {/* <Nav.Link as={NavLink} to="/passagens">Comprar passagens</Nav.Link> */}
            {/* <Nav.Link as={NavLink} to="/userP">Minhas viagens</Nav.Link> */}
<<<<<<< Updated upstream
            <Nav.Link as={NavLink} to="/adminT">Administrar Voos</Nav.Link>
            <Nav.Link as={NavLink} to="/adminC">Administrar Passagens</Nav.Link>
=======
            <Nav.Link as={NavLink} to="/adminT">Administrar voos</Nav.Link>
            <Nav.Link as={NavLink} to="/adminC">Administrar Clientes</Nav.Link>
>>>>>>> Stashed changes
            <Nav.Link as={NavLink} to="/adminA">Administrar Aeroportos</Nav.Link>
            <Nav.Link as={NavLink} to="/link">Logout</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>

    )
}



export default Menu