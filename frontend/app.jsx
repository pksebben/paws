//TODO: Implement routing for gamerprofile and shelterprofile

import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import React, { Component,Suspense,lazy } from 'react';

const Home = lazy(() => import('./views/Home.jsx'));

const App = () => (
    <Router>
      <Suspense fallback={<div>loading...</div>}>
        <Route exact path='/' component={Home}/>
      </Suspense>
    </Router>
);

export default App;
