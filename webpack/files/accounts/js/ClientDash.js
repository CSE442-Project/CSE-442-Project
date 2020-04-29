import React from "react";
import ReactDOM from "react-dom";
import "../css/style.css";
import { asyncGet, checkForErrors, processServerDateTime, serverAddressToString } from "../../shared/js/Utils";
import HeaderNav from "../../shared/js/HeaderNav";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

import ClientInfo from "./components/ClientInfo";
import ClientOrdersList from "./components/ClientOrdersList";
import ClientOrderCard from "./components/ClientOrderCard";
import OrderCreationForm from "./components/OrderCreationForm";

export default class ClientDash extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      pendingOrders: [],
      historicalOrders: [],
      clientInfo: [],
      orderFormOpen: false
    };

    this.cancelOrder = this.cancelOrder.bind(this);
    this.getOrderActionButton = this.getOrderActionButton.bind(this);
    this.orderObjectToCard = this.orderObjectToCard.bind(this);
    this.getPendingOrders = this.getPendingOrders.bind(this);
    this.getHistoricalOrders = this.getHistoricalOrders.bind(this);
    this.onOrderPlowClick = this.onOrderPlowClick.bind(this);
    this.onCloseOrderForm = this.onCloseOrderForm.bind(this);
    this.getOrders = this.getOrders.bind(this);
    this.onCreateOrder = this.onCreateOrder.bind(this);
  }

  cancelOrder(id){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, '/orders/api/cancel/' + id + "/", function(){
      if(checkForErrors(xhr)){
        this.getOrders();
      }
    }.bind(this));
  }


  getOrderActionButton(order){
    if(order.status == "U"){
      const onCancelClick = function(){
        this.cancelOrder(order.id);
      }.bind(this);
      return <Button variant="outline-primary" onClick={onCancelClick}>Cancel</Button>;
    }
    return null;
  }


  orderObjectToCard(order){
    var dt = null;
    if(order.schedule_time == null){
      dt = processServerDateTime(order.created_at);
    }else{
      dt = processServerDateTime(order.schedule_time);
    }
    var date = dt.month + "/" + dt.date + "/" + dt.year;
    var time = dt.hour + ":" + dt.minute;
    var actionButton = this.getOrderActionButton(order);
    var status = null;
    switch(order.status){
      case "U":
        status = "Unclaimed";
        break;
      case "S":
        status = "Scheduled";
        break;
      case "C":
        status = "Canceled";
        break;
      case "F":
        status = "Finished";
        break;
    }
    return <ClientOrderCard
      status={status}
      price={order.cost}
      contractor={order.contractor}
      date={date}
      time={time}
      comment={order.comment}
      vehicle={order.vehicle}
      action={actionButton}
    />;
  }


  getPendingOrders(){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, '/orders/api/pending/', function(){
      if(checkForErrors(xhr)){
        var data = JSON.parse(xhr.responseText);
        var pendingCards = data.map((item) => {
          return this.orderObjectToCard(item);
        });
        this.setState({pendingOrders: pendingCards});
      }
    }.bind(this));
  }


  getHistoricalOrders(){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, '/orders/api/historical/', function(){
      if(checkForErrors(xhr)){
        var data = JSON.parse(xhr.responseText);
        var historicalCards = data.map((item) => {
          return this.orderObjectToCard(item);
        });
        this.setState({historicalOrders: historicalCards});
      }
    }.bind(this));
  }


  onCloseOrderForm(){
    this.setState({ orderFormOpen: false });
  }


  onOrderPlowClick(){
    this.setState({ orderFormOpen: true });
  }


  getOrders(){
    this.getPendingOrders();
    this.getHistoricalOrders();
  }

  onCreateOrder(){
    this.onCloseOrderForm();
    this.getOrders();
  }


  componentDidMount(){
    this.getOrders();
  }


  render(){
    return (
      <div id="client-dash">
        <HeaderNav contractor={false}/>
        <Button variant="success" id="order-button" onClick={this.onOrderPlowClick}>Order Plow!</Button>
        <div id="pending-orders" className="section">
          <h2>Pending Orders</h2>
          <ClientOrdersList
            action={true}
            orders={this.state.pendingOrders}
          />
        </div>
        <ClientInfo />
        <div id="order-history" className="section">
          <h2>Order History</h2>
          <ClientOrdersList
            action={false}
            orders={this.state.historicalOrders}
          />
        </div>

        <Modal show={this.state.orderFormOpen} onHide={this.onCloseOrderForm}>
          <Modal.Header closeButton>
            <Modal.Title>Order Plow</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <OrderCreationForm onFinish={this.onCreateOrder}/>
          </Modal.Body>
        </Modal>
      </div>
    );
  }
}


ReactDOM.render(<ClientDash/>, document.getElementById("container"));
