/*
News Item.  This should have a single news item in it, card-style, and (maybe?) a link to a bigger article
BEN: make a design decision about whether to keep this module as-is or to contain more than one item in it (probably, make it simply *the* news module and put all functions in here)
*/

import React from 'react'

// NewsItem creates cards for a news feed
class NewsItem extends React.Component {

  render () {
    const { err, loading, news } = this.props

    if (err) {
      return <div>Error! {err.message}</div>
    }

    if (loading) {
      return <div>loading...</div>
    }

    return (
      <div>
        <h1>news title</h1>
        <p>This will be an image</p>
        <p>news snippets</p>
        <a href=''>Read the whole story</a>
      </div>
    )
  }
}


export default NewsItem;
