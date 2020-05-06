import React from "react";
import Table from "react-bootstrap/Table";

export default class ContractorOrdersList extends React.Component {

  render(){
    return (
      <div className="contractor-orders-list">
        <Table striped hover>
        <thead>
        <tr>
          <th>Price</th>
          <th>Client</th>
          <th>Address</th>
          <th>Date</th>
          <th>Time</th>
          <th>Comment</th>
          {this.props.action == true ? <th>Action</th> : null}
          {this.props.navigate == true ? <th>Navigate</th> : null}
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
