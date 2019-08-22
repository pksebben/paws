//TODO: implement some form of multiplying this in the same manner that Kirby's PHP did.

import React from 'react'


class HomeLeaderboard extends React.Component{
    render(){
        return(
            <div className="home-leaderboard leaderboard section">
              <h2 className="home-leaderboard-header">Leaderboard</h2>
              <ul className="leaderboard-list">
                
                <li className="leaderboard-list-item">
                  <a className="leaderboard-list-item-link" href="gamer_profile.php">
                  </a>
                  <span className="leaderboard-list-item-rank"></span>
                    <img className="leaderboard-list-item-avatar" src="img/placeholder-user-avatar.png"/>
                    <span className="leaderboard-list-item-name">Firstname Lastname</span>
                    <span className="leaderboard-list-item-change icon-block leaderboard-list-item-change-icon_down"></span>
                  
                  <span className="leaderboard-list-item-amount">$20,000</span>
                </li>
                
              </ul>
              
            </div>
        )
    }
}


export default HomeLeaderboard
