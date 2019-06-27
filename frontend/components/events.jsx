/*
Event module. 
This will be an encapsulated 'card' that holds data for a single event.
We may want to consider what kind of events we'll be having
*/
//TODO: Add state management

import eventdata from "./TestingData";
import React, { Component } from "react";


//Event module provides cards for event-oriented boxes, to showcase upcoming events.
class Event extends React.Component {
    render(){
        return(
            <div className="Events">
              <h1 className="Title">{this.props.title}</h1>
              <p className="Date">{this.props.date}</p>
              <p className="EventImage">{this.props.eventImage}</p>
              <p className="Description">{this.props.eventDesc}</p>
              <a className="Shelter" href={this.props.shelterLink}>{this.props.shelterName}</a>
            </div>  
        );
    }
}


export default Event;
