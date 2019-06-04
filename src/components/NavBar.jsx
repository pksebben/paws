/*
Navbar.

*/

import React, { Component } from "React";
import { Link } from "react-router-dom";

class Navbar extends React.Component {
    render(){
        return(
            <div className="Navbar">
              <Link to="./">Home</Link>
              <Link to="./GamerLogin">Gamer Login</Link>
              <Link to="./ShelterLogin">Shelter Login</Link>
            </div>  
        );
    }
}

export default Navbar;
