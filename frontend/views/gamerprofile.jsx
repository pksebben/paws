/*
  Gamer Profile.
*/
// TODO: Craft out this page according to Kirby's spec
// BEN: Gamer profile notifications have to be created.  Should they be in their own module for readability or live native in the gamer profile view?
// TODO: Do we want to make the 'upcoming fundraiser' a link to that fundraiser?
import React from 'react'
import NavBar from '../components/navbar.jsx'
import ErrorBoundary from '../components/errorboundary.jsx'

class GamerProfile extends React.Component {
    componentWillMount () {
        // set the redux store such that it knows what page you're on
    }

    render () {
        return (
            <div>
              <NavBar />
              <div id='Gamer_Profile' className='content'>
                <div className='section gamer_profile-overview'>
                  <div className='gamer_profile-overview-avatar_username'>
                    {/* THESE NEED STATE */}
                    <img className='gamer_profile-overview-avatar avatar' />
                    <h1 className='gamer_profile-overview-username'>Puggle Lover</h1>
                  </div>
                  <ul className='gamer_profile-overview-stats gamer_profile-list'>
                    <li className='gamer_profile-overview-stats-raised'>
                      <i className='icon icon-block stats-raised-icon'>moneybag</i>
                      <dl>
                        <dt>Raised</dt>
                        {/* NEEDS STATE */}
                        <dd>$3,405</dd>
                      </dl>
                    </li>
                    <li className='gamer_profile-overview-stats-rank'>
                      <i className='icon icon-block'>trophy</i>
                      <dl>
                        <dt>Rank</dt>
                        {/* NEEDS STATE */}
                        <dd>420 / 5,300</dd>
                      </dl>
                    </li>
                    <li className='gamer_profile-overview-stats-upcoming_fundraiser'>
                      <i className='icon icon-standard'>calendar</i>
                      <dl>
                        <dt>Upcoming Fundraiser</dt>
                        {/* NEEDS STATE */}
                        <dd>September 30, 2019</dd>
                      </dl>
                    </li>
                    <li className='gamer_profile-overview-stats-location'>
                      <i className='icon icon-block'>earth</i>
                      <dl>
                        <dt>Location</dt>
                        {/* NEEDS STATE */}
                        <dd>NYC</dd>
                      </dl>
                    </li>
                    <li className='gamer_profile-overview-stats-twitch_handle'>
                      <i className='icon' />
                      <dl>
                        <dt>Twitch Handle</dt>
                        {/* NEEDS STATE */}
                        <dd>Superzombiebbq</dd>
                      </dl>
                    </li>
                  </ul>
                </div>
                
                <div className='section gamer_profile-why_i_paws'>
                  <div className='why_i_paws'>
                    <header><h1>Why I Paws</h1><i className='icon' /></header>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                  </div>
                </div>


                
                <div className="gamer_profile-fundraisers">

                  <ul className="nav nav-tabs" role="tablist">
                    <li className="nav-item">
                      <a className="nav-link active" data-toggle="tab" href="#Gamer_Profile-Fundraisers-Upcoming" role="tab" aria-controls="home" aria-selected="true">Upcoming Fundraisers</a>
                    </li>
                    <li className="nav-item">
                      <a className="nav-link" data-toggle="tab" href="#Gamer_Profile-Fundraisers-Past" role="tab" aria-controls="profile" aria-selected="false">Past Fundraisers</a>
                    </li>
                  </ul>

                  <div className="tab-content" id="myTabContent">
                    <div className="tab-pane fade show active" id="Gamer_Profile-Fundraisers-Upcoming" role="tabpanel" aria-labelledby="Gamer_Profile-Fundraisers-Upcoming-tab">
                      <ul className="gamer_profile-fundraisers-upcoming-list">
                        <li className="gamer_profile-fundraisers-upcoming-date">
                          <span className="icon icon-standard">calendar</span>
                          <h3>June 30,2020</h3>
                        </li>
                        <li className="gamer_profile-fundraisers-upcoming-countdown">
                          <span className="icon icon-standard">stopwatch</span>
                          <h3 className="countdown" countdown data-date="Jun 30 2020 21:00:00">
                            <span data-days></span> Days
                            <span data-hours></span> Hours
                            <span data-minutes></span> Minutes
                            <span data-seconds></span> Seconds
                          </h3>
                        </li>
                        <li className="gamer_profile-fundraisers-upcoming-donations">
                          <span className="icon icon-block">moneybag</span>
                          <h3></h3>
                          <div className="gamer_profile-fundraisers-upcoming-donations-progress_bar"></div>
                          <button className="button button-green gamer_profile-fundraisers-upcoming-donations-donate_btn">Donate</button>
                        </li>
                        <li className="gamer_profile-fundraisers-upcoming-donors">
                          <span className="icon icon-standard">user</span>
                          <h3>45 Donations</h3>
                        </li>
                      </ul>
                      <ul className="gamer_profile-fundraisers-upcoming-share">
                        <li>
                          <a href="#"><span className="icon icon-standard">link</span> Copy Page Link</a>
                        </li>
                        <li>
                          <a href="#"><span className="icon icon-standard">calendar</span> Add to Calendar</a>
                        </li>
                        <li>
                          <a href="#"><span className="icon icon-social">facebook</span> Share to Facebook</a>
                        </li>
                      </ul>
                    </div>

                    <div className="tab-pane fade" id="Gamer_Profile-Fundraisers-Past" role="tabpanel" aria-labelledby="profile-tab">
                      <div className="gamer_profile-fundraisers-past-item">
                        <ul>
                          <li className="gamer_profile-fundraisers-past-date">
                            <span className="icon icon-standard">calendar</span>
                            <h3>August 30,2019</h3>
                          </li>
                          <li className="gamer_profile-fundraisers-past-donations">
                            <span className="icon icon-block">moneybag</span>
                            <div className="gamer_profile-fundraisers-past-donations-progress_bar"></div>
                          </li>
                          <li className="gamer_profile-fundraisers-past-donors">
                            <span className="icon icon-standard">user</span>
                            <h3>45 Donations</h3>
                          </li>
                          <div className="gamer_profile-fundraisers-past-twitch">
                          </div>
                        </ul>
                      </div>
                      <div className="gamer_profile-fundraisers-past-item">
                        <ul>
                          <li className="gamer_profile-fundraisers-past-date">
                            <span className="icon icon-standard">calendar</span>
                            <h3>August 30,2019</h3>
                          </li>
                          <li className="gamer_profile-fundraisers-past-donations">
                            <span className="icon icon-block">moneybag</span>
                            <div className="gamer_profile-fundraisers-past-donations-progress_bar"></div>
                          </li>
                          <li className="gamer_profile-fundraisers-past-donors">
                            <span className="icon icon-standard">user</span>
                            <h3>45 Donations</h3>
                          </li>
                          <div className="gamer_profile-fundraisers-past-twitch">
                          </div>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="section gamer_profile-donations">
                  <header className="gamer_profile-donations-header"><h1>Donations</h1></header>
                  <ul className="gamer_profile-donations-list">
                    <li className="gamer_profile-donations-list-item">
                      <h3 className="gamer_profile-donations-list-item-donor_name">Donor Name</h3>
                      <span className="gamer_profile-donations-list-item-amount">$45</span>
                      <date className="gamer_profile-donations-list-item-date">April 2, 2019</date>
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
