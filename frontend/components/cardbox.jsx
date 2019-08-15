/*
Cardbox provides a display for card-based modules that flexibly provides them configs and serves them up based on that config
*/

import React from 'react'

class CardBox extends React.Component {
  constructor (props) {
    super(props)
  }

  render () {
    return (
      <div>
        <h1>{this.props.boxtitle}</h1>
        {this.props.children}
      </div>
    )
  }
}

export default CardBox
