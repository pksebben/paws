/*
News Item.  This should have a single news item in it, card-style, and (maybe?) a link to a bigger article
TODO: rename 'news.jsx' to 'newsitem.jsx'
*/
//TODO: set up backend and db for news items.
//TODO: barring backend and db, create temp testing module to pass in data

import React, { Component } from "react";
import { connect } from 'react-redux';
import { fetchNews } from '../redux/actions/newsActions';

//NewsItem creates cards for a news feed
class NewsItem extends React.Component {
    componentDidMount() {
        this.props.dispatch(fetchNews());
    }
    
    render(){
        const { err, loading, news } = this.props;

        if(err) {
            return <div>Error! {err.message}</div>;
        }

        if(loading) {
            return <div>loading...</div>;
        }
        
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

const mapStateToProps = state => ({
    news: state.news.items,
    loading: state.news.loading,
    err: state.news.err
});

export default connect(mapStateToProps)(NewsItem);
