//TODO: Implement routing for gamerprofile and shelterprofile
//TODO: Git this whole project and send to kirby
//KIRBY: Hi!
//this is a test of the automated leave-fucking-files-everywhere system.
//this is another test of the alffes.
//c'mon, save already you stupid piece of..
//JUST DO IT!
//ATTAIN YOUR GOALS!
//RUNNING THROUGH THE TREES, SHIA LEBOUF!
//BITING AT YOUR KNEES, IT'S SHIA LEBOUF!
//CREEPING IN THE SHAAAAAADOWWWSSSSS...
//...HOLLYWOOD SUPERSTAR, SHIA LEBOUF!

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
