/*
Navbar.  Self-explanatory.
*/
//TODO: Fix this module such that it properly updates the store with currentpage.  Perhaps that's best done in componentdidmount in the actual page itself.
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
              <Link to="/">Home</Link>
              <Link to="/gamerprofile/">Gamer Login</Link>
              <Link to="/shelterprofile/">Shelter Login</Link>
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

