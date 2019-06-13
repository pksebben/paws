
import React from 'react';
import { render } from 'react-dom';
import App from './app.jsx';
//redux imports
import { Provider } from 'react-redux';
import store from './redux/store/index';
//TODO: delete this next import once the file is deleted. See todo from redux/index.js
import index from './redux/index';


const rootEl = document.getElementById('app');


render(
    <Provider store={ store }>
      <App />
    </Provider>
    ,rootEl);

if (module.hot) {
    module.hot.accept();
}
