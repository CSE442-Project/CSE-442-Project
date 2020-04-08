import React from "react";
import { Navbar, Nav, Button } from "react-bootstrap";
import "../css/style.css";


export default class HeaderNav extends React.Component{
	constructor(props){
		super(props);
		this.handleLogout = this.handleLogout.bind(this);
	}

	handleLogout(){
		window.location.href = '/auth/logout/'
	}

	render(){
    var dashHref = "/accounts/client/dashboard/";
    if(this.props.contractor == true){
      dashHref = "/accounts/contractor/dashboard/";
    }
		return (
        <Navbar>
          <Navbar.Brand href="/">Plow Me!</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href={dashHref}>Dashboard</Nav.Link>
            </Nav>
            <Button variant="danger" onClick={this.handleLogout}>Logout</Button>
          </Navbar.Collapse>
        </Navbar>
		);
	}
}
