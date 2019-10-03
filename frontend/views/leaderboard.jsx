/* Leaderboard View
This has all the top performing gamers and possibly others (shelters?  contributors?)
*/
import React from 'react'
import NavBar from '../components/navbar.jsx'
import ErrorBoundary from '../components/errorboundary.jsx'

class Leaderboard extends React.Component {
  render () {
    return (
      <div>
        <NavBar />
        <h1>LEADERBOARD GOES HERE</h1>
      </div>
    )
  }
}

export default Leaderboard
