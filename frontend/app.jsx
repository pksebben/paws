/*
This is where the basic routing for the app is done.  It's called by index.jsx in the same directory.
*/

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import React, { Suspense } from 'react'
import Home from './views/home.jsx'
import GamerProfile from './views/gamerprofile.jsx'
import ShelterProfile from './views/shelterprofile.jsx'
import OurTail from './views/ourtail.jsx'
import Leaderboard from './views/leaderboard.jsx'
import News from './views/news.jsx'
import './styles/styles.css'

class App extends React.Component {
  render () {
    return (
      <Router>
        <Suspense fallback={<div>loading...</div>}>
          <Switch>
            <Route exact path='/' component={Home} />
            <Route path='/gamerprofile' component={GamerProfile} />
            <Route path='/shelterprofile' component={ShelterProfile} />
            <Route path='/leaderboard' component={Leaderboard} />
            <Route path='/ourtail' component={OurTail} />
            <Route path='/news' component={News} />
          </Switch>
        </Suspense>
      </Router>
    )
  }
}

export default App
