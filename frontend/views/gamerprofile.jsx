/*
Gamer Profile.  
*/

import React, { Component } from "react";
import NavBar from '../components/navbar.jsx';
import ErrorBoundary from "../components/errorboundary.jsx";

class GamerProfile extends React.Component {
    componentWillMount(){
        //set the redux store such that it knows what page you're on
    }
    
    render() {
        return(
            <div>
              <NavBar/>
              <h1>THIS IS A PLACEHOLDER UNTIL KIRBSLICE SENDS THE ACTUAL HTML</h1>
            </div>
        );
    }
}

export default GamerProfile;
