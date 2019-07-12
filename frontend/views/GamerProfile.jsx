/*
Gamer Profile.  
*/

import React, { Component } from "react";
import NavBar from '../components/NavBar.jsx';
import ErrorBoundary from "../components/ErrorBoundary.jsx";

class GamerProfile extends React.Component {
    componentWillMount(){
        //set the redux store such that it knows what page you're on
    }
    
    render() {
        return(
            <div>
              <h1>THIS IS A PLACEHOLDER UNTIL KIRBSLICE SENDS THE ACTUAL HTML</h1>
            </div>
        );
    }
}

export default GamerProfile;
