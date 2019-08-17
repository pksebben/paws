//action constants
const SOME_ACTION = 'SOME_ACTION'

//action creators
export function someAction(somevalue) {
    return {
        type: SOME_ACTION,
        someValue
    };
}

//initialize the store with the necessary data
const initialState = {
    avatar_url: 'url of avatar', //make a default and return that for now.
    name: 'Bob Placeholder',
    total_raised: 123456789,
    rank: 1,
    upcoming_fundraiser: "IT'S THE TEN",//this is probs going to be determined from a list.  Where do?
    location: 'CRACK COMMANDMENTS',
    twitch_handle: 'TimmyPowerGamer'
};

//reducer
export default function gpo_reducer(state = initialState, action){
    switch (action.type){
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
