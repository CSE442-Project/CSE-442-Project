import React from "react";
import ReactDOM from "react-dom";
import "../css/style.css";

import Vehicles from "./components/Vehicles";
import OrdersMapList from "./components/OrdersMapList";
import MyOrders from "./components/MyOrders";

export default class ContractorDash extends React.Component {

  render(){
    return (
      <div id="contractor_dash">
        <OrdersMapList />
        <Vehicles />
        <MyOrders />
      </div>
    );
  }
}


ReactDOM.render(<ContractorDash/>, document.getElementById("container"));
