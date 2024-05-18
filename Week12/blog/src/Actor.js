import React from "react";
import './Actor.css'

class Actor extends React.Component{
    constructor(){
        super();
        this.state = {
  firstName: "George",
  lastName:"Clooney",
  url:"https://images.unsplash.com/photo-1472457897821-70d3819a0e24?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c21hbGx8ZW58MHx8MHx8fDA%3D"
        };
    }

    render() {
        return (
            <div>
                <h1>{this.state.firstName} {this.state.lastName}</h1>
                <img src={this.state.url} alt="pic"></img>
            </div>
        )
    }
}

export default Actor