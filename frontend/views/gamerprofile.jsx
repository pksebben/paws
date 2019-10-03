/*
  Gamer Profile.
*/
// TODO: Craft out this page according to Kirby's spec
// BEN: Gamer profile notifications have to be created.  Should they be in their own module for readability or live native in the gamer profile view?
// TODO: Do we want to make the 'upcoming fundraiser' a link to that fundraiser?
import React from 'react';
import NavBar from '../components/navbar.jsx';
import ErrorBoundary from '../components/errorboundary.jsx';
import GamerProfileOverview from '../components/gamerprofileoverview.jsx';
import GamerProfileFundraisers from "../components/gamerprofilefundraisers.jsx";


class GamerProfile extends React.Component {
    render () {
        return (
            <div>
              <NavBar />
              <div id='Gamer_Profile' className='content'>
                <ErrorBoundary>
                  <GamerProfileOverview/>
                </ErrorBoundary>
                <div className='section gamer_profile-why_i_paws'>
                  <div className='why_i_paws'>
                    <header><h1>Why I Paws</h1><i className='icon' /></header>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                  </div>
                </div>
                <ErrorBoundary>
                  <GamerProfileFundraisers/>
                </ErrorBoundary>
                <div className="section gamer_profile-donations">
                  <header className="gamer_profile-donations-header"><h1>Donations</h1></header>
                  <ul className="gamer_profile-donations-list">
                    <li className="gamer_profile-donations-list-item">
                      <h3 className="gamer_profile-donations-list-item-donor_name">Donor Name</h3>
                      <span className="gamer_profile-donations-list-item-amount">$45</span>
                      <ErrorBoundary>
                        <date className="gamer_profile-donations-list-item-date">April 2, 2019</date>
                      </ErrorBoundary>
                      <p className="gamer_profile-donations-list-item-comment">
                        Comment (optional) Bacon ipsum dolor amet bacon picanha ground round, ham hock occaecat swine frankfurter anim pancetta. Laborum incididunt pancetta enim pork chop eiusmod consequat ullamco meatball tenderloin officia turkey landjaeger. Commodo fatback swine jowl pork chop voluptate venison. Fatback jowl lorem prosciutto, sed ribeye quis cillum elit ground round chuck pig nulla reprehenderit. Sint consequat pancetta, landjaeger nostrud deserunt shankle short loin bacon id officia filet mignon. Kevin tenderloin buffalo ball tip, velit do cupim beef ribs quis eu minim doner.
                      </p>
                    </li>
                  </ul>
                </div>
              </div>
            </div>            
            
        )
    }
}


export default GamerProfile
