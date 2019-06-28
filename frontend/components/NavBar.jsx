/*
Navbar.  Self-explanatory.
*/

//IAN: I've put some redux testing stuff in this file.  It's where you'll see the way we connect components.
//TODO: Fix this module such that it properly updates the store with currentpage
//TODO: Disable presentation of link if user is currently on that link's page

import React, { Component } from "react";
import { Link } from "react-router-dom";
import { connect } from 'react-redux';
import { setPage } from '../redux/actions';

class Navbar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentpage: "./"
        };
        this.handleNav = this.handleNav.bind(this);
    }

    handleNav = (event) => {
        this.state.currentpage = event.target.to.pathname;
        console.log(event.target);
        this.props.setPage(this.state.currentpage );
        console.log("nav handled");
    }
    
    render(){
        return(
            <div className="Navbar">
              <Link onClick={this.handleNav} dest="home" to="./">Home</Link>
              <Link onClick={this.handleNav} dest="gamer login" to="./GamerLogin">Gamer Login</Link>
              <Link onClick={this.handleNav} dest="shelter login" to="./ShelterLogin">Shelter Login</Link>
              <h1>{this.props.currentpage}</h1>
            </div>  
        );
    }
}

const mapStateToProps = state => {
    const { currentpage } = state;
    console.log("state deconstructed.  currentpage is " + currentpage);
    return { currentpage: state.currentpage };
};

const mapDispatchToProps = {
    setPage
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Navbar);

