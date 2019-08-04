/*
Navbar.  Self-explanatory.
*/
//TODO: Check out the react-router-redux-whatever and use it so that the component knows what page it's on and doesn't serve up pointless lynx
//BEN: get rid of all that extra code I put in here to work around the link hiding problem
//TODO: replace spyglass image with the popup for searching
//IAN: potentially we might replace SIGN IN / UP with a modular, as well as DONATE.  What do you think? - ben
//TODO: Replace the 'Home' Link with the Paws logo
//TODO: Strike the 'gamerprofile' and 'shelterprofile' lynx and have those implemented via the SIGN IN / UP button.
//BEN: is there a way to implement modals without any CSS in order to test modals here?  Would it be easier just to have a little CSS in there?  Look it up.

import React, { Component } from "react";
import { Link } from "react-router-dom";
import { connect } from 'react-redux';
import { setPage } from '../redux/actions';
import ErrorBoundary from "../components/errorboundary.jsx";


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
              <Link to="/"> Home </Link>
              <Link to="/ourtail/"> Our Tail </Link>
              <Link to="/leaderboard/"> LEADERBOARD </Link>
              <Link to="/news/"> NEWS </Link>
              <ErrorBoundary>
                <img src='/path/to/spyglass.img'>search thinger</img>
              </ErrorBoundary>
              <Link to='/signin/'> SIGN IN / UP </Link>
              <Link to="/donate/"> DONATE </Link>
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

