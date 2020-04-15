import React from "react";
import { asyncPost, checkForErrors } from "../../../shared/js/Utils";



export default class OrderCreationForm extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      date: "",
      time: "",
      comment: ""
    };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
    this.handleTimeChange = this.handleTimeChange.bind(this);
    this.handleCommentChange = this.handleCommentChange.bind(this);
  }

  handleSubmit(event){
    event.preventDefault();

  }


  handleDateChange(event){
    this.setState({ date: event.target.value });
  }


  handleTimeChange(event){
    this.setState({ time: event.target.value });
  }


  handleCommentChange(event){
    this.setState({ comment: event.target.value });
  }

  render(){
    return (
      <form id="order-creation-form">

        <label>
          Date:
          <input id="order_creation_form_date" type="date" value={this.state.date} onChange={this.handleDateChange}/>
        </label>


        <label>
          Time:
          <input id="order_creation_form_time" type="time" value={this.state.time} onChange={this.handleTimeChange}/>
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
