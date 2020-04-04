import React from "react";
import ReactDOM from "react-dom";
import "../css/style.css";
import { asyncGet, checkForErrors, processServerDateTime, serverAddressToString } from "../../shared/js/Utils";
import Button from "react-bootstrap/Button";

import ContractorOrdersList from "./components/ContractorOrdersList";
import ContractorOrderCard from "./components/ContractorOrderCard";

export default class ContractorDash extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      unclaimedOrders: [],
      pendingOrders: [],
      historicalOrders: []
    };

    this.acceptOrder = this.acceptOrder.bind(this);
    this.finishOrder = this.finishOrder.bind(this);
    this.getOrderActionButton = this.getOrderActionButton.bind(this);
    this.orderObjectToCard = this.orderObjectToCard.bind(this);
    this.getUnclaimedOrders = this.getUnclaimedOrders.bind(this);
    this.getPendingOrders = this.getPendingOrders.bind(this);
    this.getHistoricalOrders = this.getHistoricalOrders.bind(this);
    this.getOrders = this.getOrders.bind(this);
  }


  acceptOrder(id){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, '/orders/api/accept/' + id + "/", function(){
      if(checkForErrors(xhr)){
        alert("Order has been accepted.");
        this.getOrders();
      }
    }.bind(this));
  }


  finishOrder(id){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, '/orders/api/finish/' + id + "/", function(){
      if(checkForErrors(xhr)){
        alert("Order has been finished.");
        this.getOrders();
      }
    }.bind(this));
  }


  getOrderActionButton(order){
    if(order.status == "U"){
      const onAcceptClick = function(){
        this.acceptOrder(order.id);
      }.bind(this);
      return <Button variant="primary" onClick={onAcceptClick}>Accept</Button>;
    }else if(order.status == "S"){
      const onFinishClick = function(){
        this.finishOrder(order.id);
      }.bind(this);
      return <Button variant="primary" onClick={onFinishClick}>Finish</Button>
    }
    return null;
  }


  orderObjectToCard(order){
    var address = serverAddressToString(order.address);
    var dt = null;
    if(order.scheduled_time == null){
      dt = processServerDateTime(order.created_at);
    }else{
      dt = processServerDateTime(order.scheduled_time);
    }
    var date = dt.month + "/" + dt.date + "/" + dt.year;
    var time = dt.hour + ":" + dt.minute;
    var actionButton = this.getOrderActionButton(order);
    return <ContractorOrderCard
      price={order.cost}
      client={order.client}
      address={address}
      date={date}
      time={time}
      comment={order.comment}
      action={actionButton}
    />;
  }


  getUnclaimedOrders(){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, '/orders/api/unclaimed/', function(){
      if(checkForErrors(xhr)){
        var data = JSON.parse(xhr.responseText);
        var unclaimedCards = data.map((item) => {
          return this.orderObjectToCard(item);
        });
        this.setState({unclaimedOrders: unclaimedCards});
      }
    }.bind(this));
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


  getOrders(){
    this.getUnclaimedOrders();
    this.getPendingOrders();
    this.getHistoricalOrders();
  }


  componentDidMount(){
    this.getOrders();
  }


  render(){
    return (
      <div id="contractor_dash">
        <div id="unclaimed-orders">
          <h2>Unclaimed Orders</h2>
          <ContractorOrdersList
            action={true}
            orders={this.state.unclaimedOrders}
          />
        </div>
        <div id="pending-orders">
          <h2>Pending Orders</h2>
          <ContractorOrdersList
            action={true}
            orders={this.state.pendingOrders}
          />
        </div>
        <div id="order-history">
          <h2>Order History</h2>
          <ContractorOrdersList
            action={false}
            orders={this.state.historicalOrders}
          />
        </div>
      </div>
    );
  }
}


ReactDOM.render(<ContractorDash/>, document.getElementById("container"));
