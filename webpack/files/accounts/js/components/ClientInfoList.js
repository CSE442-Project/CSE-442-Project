import React from "react";
import Table from "react-bootstrap/Table";

export default class ClientInfoList extends React.Component {
    render(){
        return (
            <div>
            <Table striped hover>
            <thead>
              <tr>
                <th>###</th>
                <th>User Information</th>
              </tr>
            </thead>
                {this.props.info}
            </Table>
            </div>
        );
    }
}