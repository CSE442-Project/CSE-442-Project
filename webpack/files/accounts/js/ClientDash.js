import React from "react";
import ReactDOM from "react-dom";
import "../css/style.css";
import { asyncGet, checkForErrors, processServerDateTime, serverAddressToString } from "../../shared/js/Utils";
import HeaderNav from "../../shared/js/HeaderNav";
import Button from "react-bootstrap/Button";

import ClientInfoList from "./components/ClientInfoList.js";
import ClientInfo from "./components/ClientInfoCard";
import ClientInfoCard from "./components/ClientInfoList";
import ClientOrdersList from "./components/ClientOrdersList";

export default class ClientDash extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      pendingOrders: [],
      historicalOrders: [],
      clientInfo: []
    };

    this.cancelOrder = this.cancelOrder.bind(this);
    this.getOrderActionButton = this.getOrderActionButton.bind(this);
    this.orderObjectToCard = this.orderObjectToCard.bind(this);
    this.getPendingOrders = this.getPendingOrders.bind(this);
    this.getHistoricalOrders = this.getHistoricalOrders.bind(this);
    this.getOrders = this.getOrders.bind(this);
    this.getInfo = this.getInfo.bind(this);
    this.userInfoToCard = this.userInfoToCard.bind(this);
  }

  getInfo(){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, 'accounts/api/my-info/', function(){
      if(checkForErrors(xhr)){
        var data = JSON.parse(xhr.responseText);
        var userinfo = data.map((item) => {
          return this.userInfoToCard(item);
        });
        this.setState({clientInfo: clientinfo})
      }
    }.bind(this));
  }

  userInfoToCard(client){
    var address = serverAddressToString(client.address);
    return <ClientInfoCard
      username={client.username}
      email={client.email}
      phone={client.phone}
      dw_size={client.dw_size}
      address={address}
    />;
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
    if(order.scheduled_time == null){
      dt = processServerDateTime(order.created_at);
    }else{
      dt = processServerDateTime(order.scheduled_time);
    }
    var date = dt.month + "/" + dt.date + "/" + dt.year;
    var time = dt.hour + ":" + dt.minute;
    var actionButton = this.getOrderActionButton(order);
    return <ClientOrderCard
      status={order.status}
      price={order.cost}
      contractor={order.contractor}
      date={date}
      time={time}
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


  getOrders(){
    this.getPendingOrders();
    this.getHistoricalOrders();
    this.getInfo();
  }


  componentDidMount(){
    this.getOrders();
  }


  render(){
    return (
      <div id="client-dash">
        <HeaderNav contractor={false}/>
        <div id="order-button" className="section">
          <button>Order</button>
        </div>
        <div id="client-info" className="section">
          <h2>Your Info</h2>
          <ClientInfoList
            info={this.state.clientInfo}
          />
        </div>
        <div id="pending-orders" className="section">
          <h2>Pending Orders</h2>
          <ClientOrdersList
            action={true}
            orders={this.state.pendingOrders}
          />
        </div>
        <div id="order-history" className="section">
          <h2>Order History</h2>
          <ClientOrdersList
            action={false}
            orders={this.state.historicalOrders}
          />
        </div>
      </div>
    );
  }
}


ReactDOM.render(<ClientDash/>, document.getElementById("container"));
