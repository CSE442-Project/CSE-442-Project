import React from "react";
import { asyncPost, checkForErrors, processServerDateTime } from "../../../shared/js/Utils";



export default class OrderCreationForm extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      dateTime: "",
      comment: ""
    };

    this.validateDateTime = this.validateDateTime.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleDateTimeChange = this.handleDateTimeChange.bind(this);
    this.handleCommentChange = this.handleCommentChange.bind(this);
  }

  validateDateTime(){
    if(this.state.dateTime != ""){
      var dt = processServerDateTime(this.state.dateTime);
      var jsDt = new Date(dt.year, dt.month, dt.date, dt.hour, dt.minute, 0, 0);
      var now = new Date();
      return jsDt.getTime() > now.getTime();
    }
    return true;
  }


  alertInvalidDateTime(){
    alert("Please select a preferred schedule time that is in the future or blank.")
  }


  handleSubmit(event){
    event.preventDefault();

    const validDateTime = this.validateDateTime();

    if(validDateTime){
      var xhr = new XMLHttpRequest();
      var payload = new FormData();
      if(this.state.comment != ""){
        payload.append("comment", this.state.comment);
      }
      if(this.state.dateTime != ""){
        payload.append("schedule_time", this.state.dateTime);
      }
      asyncPost(
        xhr,
        "/orders/api/create/",
        function(){
          var valid = checkForErrors(xhr);
          if(valid){
            this.props.onFinish()
          }
        }.bind(this),
        payload
      );
    }else{
      this.alertInvalidDateTime()
    }
  }


  handleDateTimeChange(event){
    this.setState({ dateTime: event.target.value });
  }


  handleCommentChange(event){
    this.setState({ comment: event.target.value });
  }

  render(){
    return (
      <form id="order-creation-form" onSubmit={this.handleSubmit}>

        <label>
          Preferred Schedule Time:
          <input id="order_creation_form_datetime" type="datetime-local" value={this.state.dateTime} onChange={this.handleDateTimeChange}/>
        </label>

        <label>
          Comment:
          <textarea id="order_creation_form_comment" value={this.state.comment} onChange={this.handleCommentChange}/>
        </label>

        <input className="form_submit" type="submit" value="Submit" />

      </form>
    );
  }
}
