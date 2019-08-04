/*
This is the core of the app, and contains all the routes to the various pages (thus, the lazy-loading)
It is also the place where appwide TODOs, IANs, BENs, and KIRBYs should live.
*/
//KIRBY: We should talk about how to do static files and such.  This is dependant on my revisiting that part of webpack
//BEN: ++PRIORITY++ Figure out webpack again so I can advise re: static files
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import React, { Component,Suspense,lazy } from 'react';

const Home = lazy(() => import(/*webpackChunkName: "Home"*/'./views/home.jsx'));
const GamerProfile = lazy(() => import(/*webpackChunkName: "GamerProfile"*/ './views/gamerprofile.jsx'));
const ShelterProfile = lazy(() => import(/*webpackChunkName: "ShelterProfile"*/'./views/shelterprofile.jsx'));
const OurTail = lazy(() => import(/*webpackChunkName: "OurTail"*/ "./views/ourtail.jsx"));
const Leaderboard = lazy(() => import(/*webpackChunkName: "Leaderboard"*/ "./views/leaderboard.jsx"));
const News = lazy(() => import(/*webPackChunkName: "News"*/ "./views/news.jsx"));

class App extends Component{
    render() {
        return(
            <Router>
              <Suspense fallback={<div>loading...</div>}>
                <Switch>
                  <Route exact path='/' component={Home}/>
                  <Route path='/gamerprofile/' component={GamerProfile}/>
                  <Route path='/shelterprofile/' component={ShelterProfile}/>
                  <Route path='/leaderboard/' component={Leaderboard}/>
                  <Route path='/ourtail/' component={OurTail}/>
                  <Route path='/news/' component={News}/>
                </Switch>
              </Suspense>
            </Router>
        );
    }
}

export default App;
