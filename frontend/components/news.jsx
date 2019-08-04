/*
News Item.  This should have a single news item in it, card-style, and (maybe?) a link to a bigger article
BEN: make a design decision about whether to keep this module as-is or to contain more than one item in it (probably, make it simply *the* news module and put all functions in here)
*/


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
