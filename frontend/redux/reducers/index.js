// This is where the redux magic happens.  Reducers take an action and use it to modify the state, the methods for doing so get defined in this file.
// GOOGLE: what directory structures are used in redux?  Can we split the reducers / actions / etc into multiple files?  What would that look like?
// GOOGLE: redux pro move - RTFM - js Object.assign().
// GOOGLE: redux pro move - RTFM - js concat() slice() ...spread
// GOOGLE: redux pro move - redux combineReducers()

import { SET_PAGE, SET_USER } from '../constants/action-types'

const initialState = {
  currentpage: 'home',
  user: null
}

// TODO: fix this switch case and test it
function rootReducer (state = initialState, action) {
  switch (action.type) {
    case SET_PAGE:
      return Object.assign({}, state, {
	    currentpage: action.payload
      })
    case SET_USER:
      /*
	  The sanity check should be done elsewhere, probably.  Middleware?
	 */
      return Object.assign({}, state, {
	    user: action.payload
      })
    default:
      return state
  }
};

export default rootReducer
