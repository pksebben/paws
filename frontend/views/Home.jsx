/*
This is the Homepage (duh.)  It's a one-to-one implementation of the IA, at the moment.  
TODO:
1. Implement some form of card container for the various elements (news, events, recent yadda, etc etc)
2. Finish factoring out the parts of the homepage into encapsulated modules
*/

import React, { Component } from "react";
import Event from "../components/events.jsx";
import OurStory from "../components/ourStory.jsx";
import NewsItem from "../components/news.jsx";
import Analytics from "../components/analytics.jsx";
import RecentGamers from "../components/recentGamers.jsx";
import RecentShelters from "../components/recentShelters.jsx";
import TopGamers from "../components/topGamers.jsx";
import { eventdata, newsdata, analyticsdata, recentgamerdata, recentshelterdata, topgamersdata } from "../components/TestingData.js";

//This is the homepage. Everything that goes in here should be modular and imported
class Home extends React.Component {
    render() {
        return(
            <div>
              <h1>
                THIS AM A HUMPAEG
              </h1>
              <OurStory/>
              <div className="upcomingEvents">
                <h1>EVENTS GO HERE</h1>
                <Event title={eventdata.title} date={eventdata.date} eventImage={eventdata.eventImage} eventDesc={eventdata.eventDesc} shelterLink={eventdata.shelterLink} shelterName={eventdata.shelterName} />
              </div>
              <div className="topGamers">
                <h1>IT PUTS THE TOP GAMERS IN THIS BASKET OR ELSE IT GETS THE HOSE AGAIN</h1>
                <TopGamers name={topgamersdata.name} shelters={topgamersdata.shelters} raised={topgamersdata.raised} events={topgamersdata.events} achievements={topgamersdata.achievements}/>
              </div>
              <h1>ANALYTICS THIS</h1>
              <Analytics amountRaised={analyticsdata.amountRaised} numGamers={analyticsdata.numGamers} numDonors={analyticsdata.numDonors} numShelters={analyticsdata.numShelters}/>
              <div className="recentlyJoinedShelters">
                <h1>GIMME RECENTLY JOINED SHELTERS</h1>
                <RecentShelters name={recentshelterdata.name} joinDate={recentshelterdata.joinDate} events={recentshelterdata.events}/>
              </div>
              <div className="recentlyJoinedGamers">
                <h1>THESE GAMERS JOINED. RECENTLY.</h1>
                <RecentGamers name={recentgamerdata.name} joinDate={recentgamerdata.joinDate}/>
              </div>
              <div className="newsCards">
                <h1>EXTRY EXTRY! DIS RIGHT HERE'S THE NEWS, GUVNAH.</h1>
                <NewsItem title={newsdata.title} snippet={newsdata.snippet} link={newsdata.link}/>
              </div>
            </div>
        );
    }

}

export default Home;
