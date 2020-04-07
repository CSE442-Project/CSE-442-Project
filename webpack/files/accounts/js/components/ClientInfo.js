import React from "react";
import Table from "react-bootstrap/Table";

export default class ClientInfo extends React.Component {
  render () {
    return (
      <div>
        <Table striped hover>
        <thead>
          <tr>
            <th>###</th>
            <th>User Information</th>
          </tr>
        <tbody>
          <tr>
            <td>Name:</td>
            <td>{this.props.user}</td>
          </tr>
          <tr>
            <td>Address:</td>
            <td>{this.props.address}</td>
          </tr>
          <tr>
            <td>Phone:</td>
            <td>{this.props.phone}</td>
          </tr>
          <tr>
            <td>Size:</td>
            <td>{this.props.dw_size}</td>
          </tr>
        </tbody>
        </Table>
      </div>
    );
  }
}
