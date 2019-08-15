/*
  This is the Homepage (duh.)  It's a one-to-one implementation of the IA, at the moment.
  TODO: Refactor this page into it's component modules
*/

import React from 'react'
import NavBar from '../components/navbar.jsx'
import Event from '../components/events.jsx'
import OurStory from '../components/ourstory.jsx'
import NewsItem from '../components/news.jsx'
import Analytics from '../components/analytics.jsx'
import RecentGamers from '../components/recentgamers.jsx'
import RecentShelters from '../components/recentshelters.jsx'
import TopGamers from '../components/topgamers.jsx'
import ErrorBoundary from '../components/errorboundary.jsx'
import CardBox from '../components/cardbox.jsx'
import { eventdata, newsdata, analyticsdata, recentgamerdata, recentshelterdata, topgamersdata } from '../components/testingdata.js'

class Home extends React.Component {
  render () {
    return (
      <div>
        <NavBar />

        {/* the mission statement is just a simple splash at the top of the page to give an idea of what we do */}
        <div id='mission_statement'>
          <h1>PLAY GAMES FOR THOSE WITHOUT A VOICE</h1>
          <p>Paws Your Game's mission is to help raise money and other resources for animal rescue organizations through video game marathons</p>
        </div>

        {/* calls to action are quick-draw buttons that immediately take you to relevant parts of the site */}
        <div id='calls_to_action'>
          <div id='donate_call'>
            <ErrorBoundary>
              <img src='donate_call_icon'>donate call img</img>
            </ErrorBoundary>
            <p>Want to help support Paws Your Game's mission in providing resources to no kill shelters?  Donate today to help support us in our mission to end kill shelters.</p>
            <button>Donate Now</button>
          </div>
        </div>

        {/* leaderboard is a breakdown of top earners */}
        <div id='leaderboard'>
          <h1>Leaderboard</h1>
          <ul id='leaderboard_board'>
            <li>gamer in place 1</li>
            <li>gamer in place 2</li>
            <li>gamer in place 3</li>
            <li>gamer in place 4</li>
            <li>gamer in place 5</li>
          </ul>
        </div>

        {/* news holds a series of news snippets.  Like an electronic presskit */}
        <div id='news'>
          <h1>PAWS IN THE NEWS</h1>
          <button id='news_scrollback_button'>gobackarrow</button>

          <div id='newsitem'>
            <h3 id='newsitem_title'>The key to victory is discipline.  And that means a well made bed.  You will practice until you can make a bed in your sleep.</h3>
            <h4 id='publisher'>publisher</h4>
            <h4 id='date'>00 / 00 / 0000</h4>
            <p id='newsitem_body' />
          </div>
          <div id='newsitem'>
            <h3 id='newsitem_title'>The key to victory is discipline.  And that means a well made bed.  You will practice until you can make a bed in your sleep.</h3>
            <h4 id='publisher'>publisher</h4>
            <h4 id='date'>00 / 00 / 0000</h4>
            <p id='newsitem_body' />
          </div>

          <div id='newsitem'>
            <h3 id='newsitem_title'>The key to victory is discipline.  And that means a well made bed.  You will practice until you can make a bed in your sleep.</h3>
            <h4 id='publisher'>publisher</h4>
            <h4 id='date'>00 / 00 / 0000</h4>
            <p id='newsitem_body' />
          </div>

        </div>

        {/* our process is a simple infographic that gives a bite-size overview of how we do */}
        <div id='ourprocess'>
          <div id='ourprocess_1'>
            <ErrorBoundary>
              <img src='/path/to/dollarsign.jpg'>dollar logo</img>
            </ErrorBoundary>
            <p>OUR MAIN GOAL IS TO PROVIDE FUNDING FOR NON-PROFIT, NO-KILL ANIMAL RESCUES AND REFUGEES THAT WILL ALLOW FOSTERS AND FACILITIES TO RESCUE MORE ANIMALS THAN EVER BEFORE</p>
          </div>

          <div id='ourprocess_2'>
            <p>WE RAISE THESE FUNDS IN MANY WAYS, THE PRIMARY SOURCE WILL BE COMMUNITY GAMING EVENTS AND MARATHONS</p>
            <ErrorBoundary>
              <img src='/path/to/controller.jpg'>controller logo</img>
            </ErrorBoundary>
          </div>

          <div id='ourprocess_3'>
            <ErrorBoundary>
              <img src='/path/to/stopwatch.jpg'>stopwatch logo</img>
            </ErrorBoundary>
            <p>PARTICIPATING GAMERS WILL BE ABLE TO FUNDRAISE FOR THE RESCUE OF THEIR CHOICE WHILE GAMING FOR 24 HOURS STRAIGHT</p>
          </div>
        </div>
      </div>
    )
  }
}

export default Home
