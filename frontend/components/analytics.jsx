/*
AnaLytics
This should be a standalone (NOT card-based) 
Might connect to store later and make stateful. idk.
*/


import React, { Component } from "react";

//Ananlytics display.  Creates cards that contain data on money raised
//and other metrics.
class Analytics extends React.Component {
    render() {
        return(
            <div className="Analytics">
              <h1 className="header">Thanks for all your support!</h1>
              <p>Raised so far: {this.props.amountRaised}</p>
              <p>Our gamer army is {this.props.numGamers} strong.</p>
              <p>{this.props.numDonors} donors have pledged their support.</p>
              <p>All of that goes to the {this.props.numShelters} shelters in our provider network.</p>
            </div>
        );
    }
}

export default Analytics;
