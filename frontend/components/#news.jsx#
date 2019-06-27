/*
News Item.  This should have a single news item in it, card-style, and (maybe?) a link to a bigger article
TODO: rename 'news.jsx' to 'newsitem.jsx'
*/
//TODO: Add state management

import React, { Component } from "react";
import { connect } from 'react-redux';

//NewsItem creates cards for a news feed
class NewsItem extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            title: this.props.title,
            
        };
    }
    
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
