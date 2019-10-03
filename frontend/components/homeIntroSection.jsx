import React from 'react'


class HomeIntroSection extends React.Component {
    render(){
        return(
            <div className="home-intro section">
              <div className="home-intro-donate_now">
                <img src="img/icon-home-intro-donate_now.png"/>
                <p>Want to help support Paws Your Game’s mission in providing resources to no kill shelters? Donate today to help support us in our mission to end kill shelters.</p>
                <button className="button" href="#">Donate Now</button>
              </div>
              <div className="home-intro-start_gaming">
                <img src="img/icon-home-intro-start_gaming.png"/>
                <p>Love playing games? Love animals? Sign up to Paws Your Game and sponsor a local no kill shelter of your choice when we have our first marathon in 2019!</p>
                <button className="button" href="#">Start Gaming</button>
              </div>
              <div className="home-intro-join_us">
                <img src="img/icon-home-intro-join_us.png"/>
                <p>Do you represent a no kill shelter? Interested in working or partnering with us? Sign up to learn more today on how you can help and support Paws Your Game.</p>
                <button className="button" href="#">Join us</button>
              </div>
            </div>
        )
    }
}


export default HomeIntroSection
