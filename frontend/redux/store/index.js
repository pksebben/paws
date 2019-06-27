//creates and exports the Redux store.  For now, it is singular and monolithic.  I am not certain but I believe that there can be more than one.

import { createStore, applyMiddleware, compose } from "redux";
import rootReducer from "../reducers/index";
import thunk from 'redux-thunk';

const storeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ ||
      compose;

const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

export default store;
