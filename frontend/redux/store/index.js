//creates and exports the Redux store.  For now, it is singular and monolithic.  I am not certain but I believe that there can be more than one.
//GOOGLE: can redux have more than one store?

import { createStore, applyMiddleware, compose } from "redux";
import rootReducer from "../reducers/index";
import { forbiddenWordsMiddleware } from '../middleware';

const storeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ ||
      compose;

const store = createStore(
    rootReducer,
    applyMiddleware(forbiddenWordsMiddleware)
);

export default store;
