import React from "react";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { Link, useMatch, useResolvedPath, NavLink } from "react-router-dom";

const Menu = ()=>{

    return(
        <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand as={NavLink} to='/'>AviaTur</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={NavLink} to="/home"> Home</Nav.Link>
            <Nav.Link as={NavLink} to="/cadastro">Cadastre-se</Nav.Link>
            <Nav.Link as={NavLink} to="/login">Login</Nav.Link>
            <Nav.Link as={NavLink} to="/passagens">Comprar passagens</Nav.Link>
            <Nav.Link as={NavLink} to="/admin">Administrar voos</Nav.Link>
            <Nav.Link as={NavLink} to="/link">Logout</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>

    )
}

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}

export default Menu