/*
  This is the Homepage (duh.)  It's a one-to-one implementation of the IA, at the moment.
  TODO: Refactor this page into it's component modules
*/

import React from 'react'
import NavBar from '../components/navbar.jsx'
import ErrorBoundary from '../components/errorboundary.jsx'
import HomeHeroSection from '../components/homeHeroSection.jsx'
import HomeIntroSection from '../components/homeIntroSection.jsx'
import HomeLeaderboard from '../components/homeLeaderboard.jsx'

class Home extends React.Component {
  render () {
    return (
      <div>
        <NavBar />
        <HomeHeroSection/>
        <HomeIntroSection/>
        <HomeLeaderboard/>
       
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
