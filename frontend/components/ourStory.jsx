import React, { Component } from "react";

//OurStory provides a simple, basic intro.  What we're about.
class OurStory extends React.Component{
    render() {
        return(
            <div className="ourStory">
              <h1>Our Story</h1>
              <p>This is Sophie. She was my best friend and first rescue pet.

                After a series of unfortunate events, I had to put Sophie to sleep due to a rare genetic disorder. My world became very dark. I became lost and shortly after attempted to take my own life.

                Because they didn’t want to see me become a statistic, my video game family stepped in and rescued me. Because of them, I entered residential treatment and turned both my passions into my purpose: Rescuing animals through playing video games.

                If every animal shelter in the United States adopted the No Kill philosphy and the programs and services that make it possible, we would save nearly three million perfectly healthy animals every year who are scheduled to die in shelters.</p>
            </div>
            
        );
    }
}

export default OurStory;