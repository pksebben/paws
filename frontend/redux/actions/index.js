//Actions take a payload and a string (which corresponds to what the action should accomplish) and uses a reducer to perform a change on the store.  I think.

import { SET_PAGE } from "../constants/action-types";

export function setPage(payload) {
    return { type: SET_PAGE, payload }
};
