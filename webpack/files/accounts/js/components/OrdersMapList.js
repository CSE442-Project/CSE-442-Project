import React from "react";
import Table from "react-bootstrap/Table";
import UnclaimedOrder from "./UnclaimedOrder";

export default class OrdersMapList extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      orders: []
    };

    this.populateUnclaimedOrders = this.populateUnclaimedOrders.bind(this);
    this.handleAcceptOrder = this.handleAcceptOrder.bind(this);
    this.getTableRows = this.getTableRows.bind(this);
  }



  handleAcceptOrder(){

  }



  populateUnclaimedOrders(){
    var xhr = XMLHttpRequest()
    xhr.open('GET', this.props.unclaimedOrdersUrl, true);
    var csrfToken = getCookie("csrftoken")
    xhr.setRequestHeader("X-CSRFToken", csrftoken);

    xhr.onload = function(){
      if(xhr.status === 200 || xhr.status === 201){
        var data = JSON.parse(xhr.responseText);
        this.setState({ orders: data });
      }else{
        alert("Server returned status code: " + xhr.status);
      }
      this.props.onFinish();
    }.bind(this);

    xhr.send(formData);
  }


  componentDidMount(){
    this.populateUnclaimedOrders();
  }


  getTableRows(){
    return this.state.orders.map((order) => {

      return <UnclaimedOrder
        price={order.cost}
        distance="N/A"
        client={order.client}
        date={}/>
    });
  }


  render(){
    return (
      <div id="orders-map-list">
        <Table striped hover>
        <thead>
        </thead>
        <tbody>
          {this.getTableRows()}
        </tbody>
        </Table>
      </div>
    );
  }
}
