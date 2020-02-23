import React from "react";
import ReactDOM from "react-dom";
import Button from "react-bootstrap/Button";


ReactDOM.render(
  (
    <div id="index_page">
      <h1>Welcome to Plow Me!</h1>
      <Button
        id="create_client_account_button"
        variant="primary">Create Client Account</Button>
      <Button
        id="create_contractor_account_button"
        variant="primary">Create Contractor Account</Button>
    </div>
  ), document.getElementById("container")
);
