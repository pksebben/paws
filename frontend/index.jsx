
import React from 'react';
import { render } from 'react-dom';
import App from './app.jsx';
//redux imports
import { Provider } from 'react-redux';
import store from './redux/store/index';
import index from './redux';

const rootEl = document.getElementById('app');

render(
    <Provider store={ store }>
      <App />
    </Provider>
    ,rootEl);

// if (module.hot) {
//     module.hot.accept();
// }
