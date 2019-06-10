/*
News Item.  This should have a single news item in it, card-style, and (maybe?) a link to a bigger article
TODO: rename 'news.jsx' to 'newsitem.jsx'
*/
import React, { Component } from "react";

//NewsItem creates cards for a news feed
class NewsItem extends React.Component {

    render(){
        return(
            <div>
              <h1>{this.props.title}</h1>
              <p>This will be an image</p>
              <p>{this.props.snippet}</p>
              <a href={this.props.link}>Read the whole story</a>
            </div>  
        );
    }
}

export default NewsItem;
