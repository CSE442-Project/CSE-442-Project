import React from "react";
import Table from "react-bootstrap/Table";

export default class ClientOrdersList extends React.Component {

  render(){
    return (
      <div className="client-orders-list">
        <Table striped hover>
        <thead>
        <tr>
          <th>Status</th>
          <th>Cost</th>
          <th>Contractor</th>
          <th>Date</th>
          <th>Time</th>
          <th>Comment</th>
          {this.props.action == true ? <th>Action</th> : null}
        </tr>
        </thead>
        <tbody>
          {this.props.orders}
        </tbody>
        </Table>
      </div>
    );
  }
}
