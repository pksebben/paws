import React from 'react'


class GamerProfileFundraisers extends React.Component{
    render() {
        return(
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
        )
    }
}

export default GamerProfileFundraisers
