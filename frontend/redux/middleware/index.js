import { ADD_FHQWHGADS } from '../constants/action-types';

const forbiddenWords = ["maga","trump"];

export function forbiddenWordsMiddleware( {dispatch} ) {
    return function(next){
	return function(action){
	    //do stuffs
	    if (action.type === ADD_FHQWHGADS) {

		const foundWord = forbiddenWords.filter(word =>
							action.payload.title.includes(word));

		if(foundWord.length) {
		    return dispatch({ type: "FOUND_BAD_WORD"});
		}
	    }
	    return next(action);
	};
    };
}
