import React from "react";
import Table from "react-bootstrap/Table";

export default class ClientInfo extends React.Component {
  render () {
    return (
      <tbody>
      <tr>
        <td>Name:</td>
        <td>{this.props.username}</td>
      </tr>
      <tr>
        <td>Email:</td>
        <td>{this.props.email}</td>
      </tr>
      <tr>
        <td>Phone:</td>
        <td>{this.props.phone}</td>
      </tr>
      <tr>
        <td>Size:</td>
        <td>{this.props.dw_size}</td>
      </tr>
      <tr>
        <td>Address:</td>
        <td>{this.props.address}</td>
      </tr>
      </tbody>
    );
  }
}
