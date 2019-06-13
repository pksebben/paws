//creates and exports the Redux store.  For now, it is singular and monolithic.  I am not certain but I believe that there can be more than one.
//GOOGLE: can redux have more than one store?

import { createStore } from "redux";
import rootReducer from "../reducers/index";

const store = createStore(rootReducer);

export default store;
