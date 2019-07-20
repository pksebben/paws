/*
This is the Homepage (duh.)  It's a one-to-one implementation of the IA, at the moment.  
TODO:
1. Implement some form of card container for the various elements (news, events, recent yadda, etc etc)
2. Finish factoring out the parts of the homepage into encapsulated modules
*/

import React, { Component } from "react";
import NavBar from '../components/navbar.jsx';
import Event from "../components/events.jsx";
import OurStory from "../components/ourstory.jsx";
import NewsItem from "../components/news.jsx";
import Analytics from "../components/analytics.jsx";
import RecentGamers from "../components/recentgamers.jsx";
import RecentShelters from "../components/recentshelters.jsx";
import TopGamers from "../components/topgamers.jsx";
import ErrorBoundary from "../components/errorboundary.jsx";
import CardBox from "../components/cardbox.jsx";
import { eventdata, newsdata, analyticsdata, recentgamerdata, recentshelterdata, topgamersdata } from "../components/testingdata.js";



class Home extends React.Component {
    render() {
        return(
            <div>
              <NavBar/>
              <h1>
                Homepage
              </h1>
              <OurStory/>
              <CardBox boxtitle="Upcoming Events">
                <Event title={eventdata.title} date={eventdata.date} eventImage={eventdata.eventImage} eventDesc={eventdata.eventDesc} shelterLink={eventdata.shelterLink} shelterName={eventdata.shelterName} />
              </CardBox>
              <div className="topGamers">
                <h1>Professional Top Gamers</h1>
                <TopGamers name={topgamersdata.name} shelters={topgamersdata.shelters} raised={topgamersdata.raised} events={topgamersdata.events} achievements={topgamersdata.achievements}/>
              </div>
              <h1>Professional Analytics</h1>
              <Analytics amountRaised={analyticsdata.amountRaised} numGamers={analyticsdata.numGamers} numDonors={analyticsdata.numDonors} numShelters={analyticsdata.numShelters}/>
              <div className="recentlyJoinedShelters">
                <h1>Professional Recently Joined Shelters</h1>
                <RecentShelters name={recentshelterdata.name} joinDate={recentshelterdata.joinDate} events={recentshelterdata.events}/>
              </div>
              <div className="recentlyJoinedGamers">
                <h1>Professional Gamers Who May Or May Not Have Recently Joined</h1>
                <RecentGamers name={recentgamerdata.name} joinDate={recentgamerdata.joinDate}/>
              </div>
              <ErrorBoundary>
                <div className="newsCards">
                  <h1>Professional News</h1>
                  <NewsItem title={newsdata.title} snippet={newsdata.snippet} link={newsdata.link}/>
                </div>
              </ErrorBoundary>
            </div>
        );
    }

}

export default Home;
