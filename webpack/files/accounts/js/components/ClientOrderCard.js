import React from "react";

export default class ClientOrderCard extends React.Component {

  render(){
    return (
      <tr>
        <td>{this.props.status}</td>
        <td>${this.props.price}</td>
        <td>{this.props.contractor}</td>
        <td>{this.props.date}</td>
        <td>{this.props.time}</td>
        <td>{this.props.comment}</td>
        <td>{this.props.vehicle}</td>
        {this.props.action != null ? <td>{this.props.action}</td> : null}
      </tr>
    );
  }
}
