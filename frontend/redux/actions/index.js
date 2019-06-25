//Actions take a payload and a string (which corresponds to what the action should accomplish) and uses a reducer to perform a change on the store.  I think.

import { ADD_FHQWHGADS, SET_PAGE } from "../constants/action-types";

//because we expect each fhqwhgads to have an id and a title, these payloads (determined at dispatch) must have those
export function addFhqwhgads(payload) {
    return { type: ADD_FHQWHGADS, payload }
};

export function setPage(payload) {
    return { type: SET_PAGE, payload }
};
