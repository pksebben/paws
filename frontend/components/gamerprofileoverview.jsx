import React from 'react';
import ErrorBoundary from './errorboundary.jsx';
import { connect } from 'react-redux';
import { testAction } from '../redux/ducks/gamerprofileoverview_duck.js';

function mapStateToProps(state) {
    return {
        gpo: state.gpo
    };
}

function mapDispatchToProps(dispatch) {
    return {
        testAction: (value) => dispatch(testAction(value))
    };
}

class GamerProfileOverview extends React.Component{

    testFunction = (event) => {
        event.preventDefault();
        this.props.testAction(event.target.value);
    }
    
    render() {
        console.log("THIS PROPS GPO");
        console.log(this.props.gpo);
        console.log("CHANGE TESTVALUE TO 5");

        return(
            <div className='section gamer_profile-overview'>
              <button value={10} onClick={this.testFunction}>TEST ME</button>
              <div className='gamer_profile-overview-avatar_username'>
                <img className='gamer_profile-overview-avatar avatar' /> {/* stateful */}
                <h1 className='gamer_profile-overview-username'>{this.props.gpo.name}</h1> {/* stateful */}
              </div>
              <ul className='gamer_profile-overview-stats gamer_profile-list'>
                <li className='gamer_profile-overview-stats-raised'>
                  <i className='icon icon-block stats-raised-icon'>moneybag</i> {/* static */}
                  <dl>
                    <dt>Raised</dt>
                    <dd>{this.props.gpo.total_raised}</dd> {/* stateful */}
                  </dl>
                </li>
                <li className='gamer_profile-overview-stats-rank'>
                  <i className='icon icon-block'>trophy</i> {/* static */}
                  <dl>
                    <dt>Rank</dt>
                    <dd>{this.props.gpo.rank} / 5,300</dd> {/* stateful */}
                  </dl>
                </li>
                <li className='gamer_profile-overview-stats-upcoming_fundraiser'>
                  <i className='icon icon-standard'>calendar</i> {/* static */}
                  <dl>
                    <dt>Upcoming Fundraiser</dt>
                    <dd>{this.props.gpo.upcoming_fundraiser}</dd> {/* stateful */}
                  </dl>
                </li>
                <li className='gamer_profile-overview-stats-location'>
                  <i className='icon icon-block'>earth</i> {/* static */}
                  <dl>
                    <dt>Location</dt>
                    <dd>{this.props.gpo.location}</dd> {/* stateful */}
                  </dl>
                </li>
                <li className='gamer_profile-overview-stats-twitch_handle'>
                  <i className='icon' /> {/* static */}
                  <dl>
                    <dt>Twitch Handle</dt>
                    <dd>{this.props.gpo.twitch_handle}</dd> {/* stateful */}
                  </dl>
                </li>
              </ul>
            </div>          
        );
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(GamerProfileOverview);
