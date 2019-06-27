//This is where the redux magic happens.  Reducers take an action and use it to modify the state, the methods for doing so get defined in this file.
//GOOGLE: what directory structures are used in redux?  Can we split the reducers / actions / etc into multiple files?  What would that look like?
//GOOGLE: redux pro move - RTFM - js Object.assign().
//GOOGLE: redux pro move - RTFM - js concat() slice() ...spread
//GOOGLE: redux pro move - redux combineReducers()

import { ADD_FHQWHGADS, SET_PAGE, FOUND_BAD_WORD } from "../constants/action-types";

const initialState = {
    fhqwhgads: [],
    currentpage: "home",
};

//TODO: fix this switch case and test it
function rootReducer(state = initialState, action) {
    switch (action.type) { 
    case ADD_FHQWHGADS:
	return Object.assign({}, state, {
	    fhqwhgads: state.fhqwhgads.concat(action.payload)
	});
    case SET_PAGE:
	return Object.assign({}, state, {
	    currentpage: action.payload
	})
    case FOUND_BAD_WORD:
	alert((Array(11).join("robin" - 2) + " batman!").toString());
	return state;
    default:
	return state;
    }
};

export default rootReducer;
