import React from "react";


export default class ContractorOrderCard extends React.Component {

  render(){
    return (
      <tr>
        <td>${this.props.price}</td>
        <td>{this.props.client}</td>
        <td>{this.props.address}</td>
        <td>{this.props.date}</td>
        <td>{this.props.time}</td>
        <td>{this.props.comment}</td>
        {this.props.action != null ? <td>{this.props.action}</td> : null}
        {this.props.navigate != null ? <td>{this.props.navigate}</td> : null}
      </tr>
    );
  }
}
