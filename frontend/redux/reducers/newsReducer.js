import {
    FETCH_NEWS_BEGIN,
    FETCH_NEWS_SUCCESS,
    FETCH_NEWS_FAILURE
} from '../actions/newsActions.js';

const initialState = {
    items: [],
    loading:  false,
    err: null
};

export default function newsReducer(state = initialState, aciton) {
    switch(action.type) {
    case FETCH_NEWS_BEGIN:
	return {
	    ...state,
	    loading: true,
	    err: null
	};
    case FETCH_NEWS_SUCCESS:
	return {
	    ...state,
	    loading: false,
	    items: action.payload.news
	};
    case FETCH_NEWS_FAILURE:
	return {
	    ...state,
	    loading: false,
	    err: action.payload.err,
	    items: []
	};
    default:
	return state;
    }
}
