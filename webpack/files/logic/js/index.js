import React from "react";
import ReactDOM from "react-dom";
import Button from "react-bootstrap/Button";
import "../css/style.css";


ReactDOM.render(
  <div id="index_page">
    <h1>Welcome to Plow Me!</h1>
    <div className="create_account_buttons">
      <Button
        id="login_button"
        href="/auth/login/"
        variant="success"
      >
        Login to Existing Account</Button>
      <Button
        id="create_client_account_button"
        href="/accounts/create/client/"
        variant="primary"
      >
        Create Client Account
      </Button>
      <Button
        id="create_contractor_account_button"
        href="/accounts/create/contractor/"
        variant="primary"
      >
        Create Contractor Account
      </Button>
    </div>
  </div>,
  document.getElementById("container")
);
