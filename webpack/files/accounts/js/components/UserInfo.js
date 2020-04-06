import React from "react";
import Table from "react-bootstrap/Table";

export default class UserInfo extends React.Component {
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
            <td></td>
          </tr>
          <tr>
            <td>Address:</td>
            <td></td>
          </tr>
          <tr>
            <td>Phone:</td>
            <td></td>
          </tr>
          <tr>
            <td>Size:</td>
            <td></td>
          </tr>
        </tbody>
        </Table>
      </div>
    )
  }
}
