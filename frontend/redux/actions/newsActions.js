export function fetchNews () {
  return dispatch => {
    dispatch(fetchNewsBegin())
    return fetch('/news')
	    .then(res => res.json())
	    .then(json => {
        dispatch(fetchNewsSuccess(json.news))
        return json.news
	    })
	    .catch(err => dispatch(fetchNewsFailure(err)))
  }
}

export const FETCH_NEWS_BEGIN = 'FETCH_NEWS_BEGIN'
export const FETCH_NEWS_SUCCESS = 'FETCH_NEWS_SUCCESS'
export const FETCH_NEWS_FAILURE = 'FETCH_NEWS_FAILURE'

export const fetchNewsBegin = () => ({
  type: FETCH_NEWS_BEGIN
})

export const fetchNewsSuccess = news => ({
  type: FETCH_NEWS_SUCCESS,
  payload: { news }
})

export const fetchNewsFailure = err => ({
  type: FETCH_NEWS_FAILURE,
  payload: { err }
})
