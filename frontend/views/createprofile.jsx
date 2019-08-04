import React, {Component} from "react";
import NavBar from "../components/navbar.jsx";
import ErrorBoundary from "../components/errorboundary.jsx";
//TODO: complete this module
//KIRBY: I'm wondering if the best way to do this bit is to have some CSS that hides or shows elements.  Is this simple / quick to implement?  What are your thoughts? -B

class CreateProfile extends React.Component {
    render(){
        return(
            <div>
              <NavBar/>
              {/*  are we going to do a modal here?  How much of this can be done in CSS?*/}
            </div>
        );
    }
}


export default CreateProfile;
