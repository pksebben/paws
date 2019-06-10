/*
Top Gamers Module.  This generates a card that gets put in a cardbox.
*/

import React, { Component } from "react";

//TopGamers creates cards that track and display the top earning gamers on the site
class TopGamers extends React.Component {
    render() {
        return(
            <div>
              <p>This gonna be an avatar</p>
              <p>{this.props.name}</p>
              <p>{this.props.raised}</p>
              <p>{this.props.shelters}</p>
              <p>{this.props.events}</p>
              <p>{this.props.achievements}</p>
            </div>  
        );
    }
}

export default TopGamers;
