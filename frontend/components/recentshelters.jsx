/*
Recent shelter module provides cards on recently joined shelters
card-style?
*/

import React from 'react'

class RecentShelters extends React.Component {
  render () {
    return (
      <div>
        <p>This will be an avatar</p>
        <p>{this.props.name}</p>
        <p>{this.props.joinDate}</p>
        <p>{this.props.events}</p>
      </div>
    )
  }
}

export default RecentShelters
