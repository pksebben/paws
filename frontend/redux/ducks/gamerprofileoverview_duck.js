//action constants
const TEST_ACTION = 'TEST_ACTION'

//action creators
export function testAction(value) {
    return {
        type: TEST_ACTION,
        value
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
    twitch_handle: 'TimmyPowerGamer',
    test_value: 0
};

//reducers. This is where the logic goes.
export default function gpo_reducer(state = initialState, action){
    switch (action.type){
    case 'TEST_ACTION':
        return Object.assign({}, state, {
            test_value: action.value
        })
    default:
        return state;
    }
}
