/* News Views
Paws your game in the news!  Perhaps also news items we wish to self-publish.  Needs some thinking.
*/

import React from 'react'
import NavBar from '../components/navbar.jsx'
import ErrorBoundary from '../components/errorboundary.jsx'

class News extends React.Component {
  render () {
    return (
      <div>
        <NavBar />
        <h1>NEWS GOES HERE</h1>
      </div>
    )
  }
}

export default News
