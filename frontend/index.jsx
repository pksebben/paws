import React from 'react';
import ReactDOM from 'react-dom';
import App from './app.jsx';
// redux imports
import { Provider } from 'react-redux';
import configureStore from './redux/configurestore';

let store = configureStore();

//make the store accessible in the console for debugging
window.store = store;

class Paws extends React.Component {
    render(){
        return(
            <Provider store={store}>
              <App />
            </Provider>
        );
    }
}

ReactDOM.render(<Paws />, document.getElementById('app'));
