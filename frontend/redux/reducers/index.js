//This is where the redux magic happens.  Reducers take an action and use it to modify the state, the methods for doing so get defined in this file.
//GOOGLE: what directory structures are used in redux?  Can we split the reducers / actions / etc into multiple files?  What would that look like?
//GOOGLE: redux pro move - RTFM - js Object.assign().
//GOOGLE: redux pro move - RTFM - js concat() slice() ...spread
//GOOGLE: redux pro move - redux combineReducers()

import { ADD_ARTICLE } from "../constants/action-types";

const initialState = {
    articles: []
};

function rootReducer(state = initialState, action) {
    if (action.type === ADD_ARTICLE) {
	return Object.assign({}, state, {
	    articles: state.articles.concat(action.payload)
	});
    }
    return state;
};

export default rootReducer;
