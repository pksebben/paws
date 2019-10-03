import { createStore, applyMiddleware, combineReducers } from 'redux';
import { createLogger } from 'redux-logger';
import gpo_reducer from './ducks/gamerprofileoverview_duck.js';

const loggerMiddleWare = createLogger();

const createStoreWithMiddleWare = applyMiddleware(loggerMiddleWare)(createStore);

const rootReducer = combineReducers({
    gpo: gpo_reducer
})

const configureStore = (initialState) => createStoreWithMiddleWare(rootReducer, initialState);
export default configureStore;
