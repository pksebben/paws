/*
Gamer Profile.  
*/
//TODO: Craft out this page according to Kirby's spec
//BEN: Gamer profile notifications have to be created.  Should they be in their own module for readability or live native in the gamer profile view?
//TODO: Do we want to make the 'upcoming fundraiser' a link to that fundraiser?
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
              <div id="Gamer_Profile" className="content">
                <div className="section gamer_profile-overview">
                  <div className="gamer_profile-overview-avatar_username">
                    {/* THESE NEED STATE */}
                    <img className="gamer_profile-overview-avatar avatar"/>
                    <h1 className="gamer_profile-overview-username">Puggle Lover</h1>
                  </div>
                  <ul className="gamer_profile-overview-stats gamer_profile-list">
                    <li className="gamer_profile-overview-stats-raised">
                      <i className="icon icon-block stats-raised-icon">moneybag</i>
                      <dl>
                        <dt>Raised</dt>
                        {/* NEEDS STATE */}
                        <dd>$3,405</dd>
                      </dl>
                    </li>
                    <li className="gamer_profile-overview-stats-rank">
                      <i className="icon icon-block">trophy</i>
                      <dl>
                        <dt>Rank</dt>
                        {/* NEEDS STATE */}
                        <dd>420 / 5,300</dd>
                      </dl>
                    </li>
                    <li className="gamer_profile-overview-stats-upcoming_fundraiser">
                      <i className="icon icon-standard">calendar</i>
                      <dl>
                        <dt>Upcoming Fundraiser</dt>
                        {/* NEEDS STATE */}
                        <dd>September 30, 2019</dd>
                      </dl>
                    </li>
                    <li className="gamer_profile-overview-stats-location">
                      <i className="icon icon-block">earth</i>
                      <dl>
                        <dt>Location</dt>
                        {/* NEEDS STATE */}
                        <dd>NYC</dd>
                      </dl>
                    </li>
                    <li className="gamer_profile-overview-stats-twitch_handle">
                      <i className="icon"></i>
                      <dl>
                        <dt>Twitch Handle</dt>
                        {/* NEEDS STATE */}
                        <dd>Superzombiebbq</dd>
                      </dl>
                    </li>
                  </ul>
                </div>
                <div className="section gamer_profile-why_i_paws">
                  <div className="why_i_paws">
                    <header><h1>Why I Paws</h1><i className="icon"></i></header>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                  </div>
                </div>
              </div>
            </div>
        );
    }
}

export default GamerProfile;
