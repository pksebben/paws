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
