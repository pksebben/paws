//TODO: Implement routing for gamerprofile and shelterprofile
//TODO: Git this whole project and send to kirby
//KIRBY: Hi!

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import React, { Component,Suspense,lazy } from 'react';

const Home = lazy(() => import('./views/Home.jsx'));
// const GamerProfile = lazy(() => import('./views/GamerProfile.jsx'));
// const ShelterProfile = lazy(() => import('./views/ShelterProfile.jsx'));

const App = () => (
    <Router>
      <Suspense fallback={<div>loading...</div>}>
        <Route exact path='/' component={Home}/>
        {/* <Route path='/GamerProfile' component={GamerProfile}/> */}
        {/* <Route path='/ShelterProfile' component={ShelterProfile}/> */}
      </Suspense>
    </Router>
);

export default App;
