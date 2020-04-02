import React from "react";
import Button from "react-bootstrap/Button";
import Table from "react-bootstrap/Table";
import { getCookie, csrfSafeMethod } from "../../../shared/js/Cookies";


export default class UnclaimedOrder extends React.Component {
  constructor(props){
    super(props);

    this.onAccept = this.onAccept.bind(this);
  }


  onAccept(){
    var xhr = XMLHttpRequest()
    xhr.open('GET', this.props.acceptUrl, true);
    var csrfToken = getCookie("csrftoken")
    xhr.setRequestHeader("X-CSRFToken", csrftoken);

    xhr.onload = function(){
      if(xhr.status === 200 || xhr.status === 201){
        this.props.handleAccept();
      }else{
        alert("Server returned status code: " + xhr.status);
      }
      this.props.onFinish();
    }.bind(this);

    xhr.send(formData);
  }


  render(){
    return (
      <tr>
        <td>{this.props.price}</td>
        <td>{this.props.distance}</td>
        <td>{this.props.client}</td>
        <td>{this.props.date}</td>
        <td>{this.props.time}</td>
        <td><Button variant="primary" onClick={this.onAccept}>Accept</Button></td>
      </tr>
    );
  }
}
