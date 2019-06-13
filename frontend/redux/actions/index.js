//Actions take a payload and a string (which corresponds to what the action should accomplish) and uses a reducer to perform a change on the store.  I think.

import { ADD_ARTICLE } from "../constants/action-types";

export function addArticle(payload) {
    return { type: ADD_ARTICLE, payload }
};
