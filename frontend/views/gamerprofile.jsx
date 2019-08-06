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
            <div id="Gamer_Profile" className="content">
              <div className="section gamer_profile-overview">
                <div className="gamer_profile-overview-avatar_username">
                  <img className="gamer_profile-overview-avatar avatar"/>
                  <h1 className="gamer_profile-overview-username">Puggle Lover</h1>
              </div>
              <ul className="gamer_profile-overview-stats gamer_profile-list">
                <li className="gamer_profile-overview-stats-raised">
                  <i className="icon icon-block stats-raised-icon">moneybag</i>
                  <dl>
                    <dt>Raised</dt>
                    <dd>$3,405</dd>
                  </dl>
                </li>
                <li className="gamer_profile-overview-stats-rank">
                  <i className="icon icon-block">trophy</i>
                  <dl>
                    <dt>Rank</dt>
                    <dd>420 / 5,300</dd>
                  </dl>
                </li>
                <li className="gamer_profile-overview-stats-upcoming_fundraiser">
                  <i className="icon icon-standard">calendar</i>
                  <dl>
                    <dt>Upcoming Fundraiser</dt>
                    <dd>September 30, 2019</dd>
                  </dl>
                </li>
                <li className="gamer_profile-overview-stats-location">
                  <i className="icon icon-block">earth</i>
                  <dl>
                    <dt>Location</dt>
                    <dd>NYC</dd>
                  </dl>
                </li>
                <li className="gamer_profile-overview-stats-twitch_handle">
                  <i className="icon"></i>
                  <dl>
                    <dt>Twitch Handle</dt>
                    <dd>Superzombiebbq</dd>
                  </dl>
                </li>
              </ul>
            </div> 
            </div>
        );
    }
}

export default GamerProfile;
