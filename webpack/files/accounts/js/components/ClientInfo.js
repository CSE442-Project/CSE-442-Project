import React from "react";
import { asyncGet, checkForErrors, serverAddressToString } from "../../../shared/js/Utils";



export default class ClientInfo extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      username: null,
      phone: null,
      drivewaySize: null,
      rate: null,
      email: null,
      address: null
    };

    this.getInfo = this.getInfo.bind(this);
  }


  getInfo(){
    var xhr = new XMLHttpRequest()
    asyncGet(xhr, '/accounts/api/my-info/?format=json', function(){
      if(checkForErrors(xhr)){
        var data = JSON.parse(xhr.responseText);
        this.setState({
          username: data.username,
          phone: data.phone,
          email: data.email,
          drivewaySize: data.dw_size,
          rate: data.dw_size * 15,
          address: serverAddressToString(data.address)
        });
      }
    }.bind(this));
  }


  componentDidMount(){
    this.getInfo();
  }


  render(){
    return (
      <div id="client-info" className="section">
        <h2>Your Info</h2>
        <div id="info">
          <h5 className="info-entry">Username: {this.state.username}</h5>
          <h5 className="info-entry">Email: {this.state.email}</h5>
          <h5 className="info-entry">Driveway Size: {this.state.drivewaySize}</h5>
          <h5 className="info-entry">Flat Rate: {this.state.rate}</h5>
          <h5 className="info-entry">Address: {this.state.address}</h5>
        </div>
      </div>
    );
  }
}
