/*
Gamer Profile.  
*/
//TODO: Craft out this page according to Kirby's spec
//BEN: Gamer profile notifications have to be created.  Should they be in their own module for readability or live native in the gamer profile view?
//KIRBY:So this is the first place that it's plainly obvious that I am not yet qualified to write HTML.  I have *no idea* how to deal with things like the summary (where it's all money raised, avatar, name, next event, etc.).  I know how to get it done with a fuckton of nested divs but that seems like a good way to raise your blood pressure and create a clusterfuck.  When we sit down tomorrow (or whenever we get to it) I wanna try and attack this problem with extreme prejudice.  Perhaps one way to do that is to have you write up a couple examples (as if we were just gonna have you do it) and see if I can work from there.  If this tack feels like too much of a pain in the ass, just LMK and we can approach this whatever way you desire.  I would like to take some of the HTMLing load off you if I can but if we decide that's the hard way I have no ego about the matter.  I suppose it also goes without saying that this module is incomplete
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

              <div id="notifications">CREATE NOTIFICATION MODULE AND PLACE HERE</div>

              <div id="profilesummary">
                <ErrorBoundary>
                  <div id="avatar">
                    <img src="/path/to/avatar.jpg"/>
                    <h2>Gamer Name goes here</h2>
                  </div>
                </ErrorBoundary>
                <div id="profile_infotable">
                  <div id="moneyraised">
                    <ErrorBoundary>
                        <img src="/path/to/money.jpg"/>
                    </ErrorBoundary>
                    <h1>Raised: $money</h1>
                  </div>
                </div>
              </div>
              <h1>THIS IS WHERE THE GAMER PROFILE GOES</h1>
            </div>
        );
    }
}

export default GamerProfile;
