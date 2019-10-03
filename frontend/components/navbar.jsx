/*
Navbar.  Self-explanatory.
*/
//TODO: Check out the react-router-redux-whatever and use it so that the component knows what page it's on and doesn't serve up pointless lynx
//TODO: replace spyglass image with the popup for searching
//BEN: is there a way to implement modals without any CSS in order to test modals here?  Would it be easier just to have a little CSS in there?  Look it up.

import React from "react";
import { Link } from "react-router-dom";
import ErrorBoundary from "../components/errorboundary.jsx";


class Navbar extends React.Component {

    render(){
        return(
            <nav id="Nav">
              <h1 className="nav-logo">Paws Your Game</h1>
              <ul>
                <li><Link to="/"> Home </Link></li>
                <li><Link to="/ourtail/"> Our Tail </Link></li>
                <li><Link to="/leaderboard/"> LEADERBOARD </Link></li>
                <li><Link to="/news/"> NEWS </Link></li>
                <ErrorBoundary>
                  <li className="nav-search">
                    <form>
                      <button>
                        <i className="icon icon-standard">search</i>
                      </button>
                      <input type="text" name="search" placeholder={"Search for players, shelters, or donors."}/>
                    </form>
                  </li>
                </ErrorBoundary>
                <li className="nav-signin"><Link to='/signin/'> SIGN IN / UP </Link></li>
                <li className="nav-donate"><Link to="/donate/"> DONATE </Link></li>
              </ul>
            </nav>  
        );
    }
}


export default Navbar;
