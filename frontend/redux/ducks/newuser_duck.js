//action constants
const MAKE_USER_REQUEST = 'MAKE_USER_REQUEST'
const MAKE_USER_FAILURE = 'MAKE_USER_FAILURE'
const MAKE_USER_SUCCESS = 'MAKE_USER_SUCCESS'

//action creators
export function makeUserRequest(user_data) {
    return {
        type: MAKE_USER_REQUEST,
        user_data
    };
}

export function makeUserFailure(err) {
    return {
        type: MAKE_USER_FAILURE,
        err
    };
}

export function makeUserSuccess(res) {
    return {
        type: MAKE_USER_SUCCESS,
        res
    };
}

//initialize the store with the necessary data
const initialState = {
    crudc_user_name = null,
    crudc_user_password = null,
    crudc_user_email = null,
};

//reducer
export default function reducer(state = initialState, action){
    switch (action.type){
    case MAKE_USER_REQUEST:
        return Object.assign(
            {},
            state,
            {
                crudc_user_name: action.user_data.name,
                crudc_user_email: action.user.email,
                crudc_user_password: action.user.password
            }
        )
        //MAKE AJAX REQUEST HERE?
    default:
        return state;
    }
}

/*
the patterns herein were gleaned from here: https://github.com/goopscoop/ga-react-tutorial/

this pattern requires the following in other files:

in redux/configureStore.js ~~~~~~~~~~~~~~~~~~~~
a configurestore that uses combinereducers to create the initial store, and may apply middleware

in the components that use the store ~~~~~~~~~~~~~~~~~~~~
mapStateToProps functions that give the component access to the store
mapDispatchToProps functions that allow changes in the store to be made based on changes in the props of components.
a connect function that replaces the default export

note:  There is, in that tutorial, a container that extracts all the functions from the module and connects them to the state outside of the module.  IDK why we would do this, save for making things more readable when there is a huge singular module (which we are trying to avoid anyhow.)

*/
