
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import React, { Component,Suspense,lazy } from 'react';

const Home = lazy(() => import(/*webpackChunkName: "Home"*/'./views/Home.jsx'));
const GamerProfile = lazy(() => import(/*webpackChunkName: "GamerProfile"*/ './views/GamerProfile.jsx'));
const ShelterProfile = lazy(() => import(/*webpackChunkName: "ShelterProfile"*/'./views/ShelterProfile.jsx'));

class App extends Component{
    render() {
        return(
            <Router>
              <Suspense fallback={<div>loading...</div>}>
                <Switch>
                  <Route exact path='/' component={Home}/>
                  <Route path='/gamerprofile/' component={GamerProfile}/>
                  <Route path='/shelterprofile/' component={ShelterProfile}/>
                </Switch>
              </Suspense>
            </Router>
        );
    }
}

export default App;
