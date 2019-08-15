/*
Recent Gamers module creates cards that display recently joined gamers
Card-style.  To be invoked by a cardbox.  Shows the data for recently joined gamers
Maybe the basis for who to show should be some combination of recency and whether they got an upcoming thing
*/

import React from 'react'

class RecentGamers extends React.Component {
  render () {
    return (
      <div>
        <p>Highly professional avatar goes here</p>
        <h2 className='Name'>{this.props.name}</h2>
        <p>{this.props.joinDate}</p>
        <ul>
          <li>Put the upcoming events here.</li>
        </ul>
      </div>
    )
  }
}

export default RecentGamers
