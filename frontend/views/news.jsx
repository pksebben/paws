/*News Views
Paws your game in the news!  Perhaps also news items we wish to self-publish.  Needs some thinking.
*/
//TODO: Fix up the news component and figure out a way to either use it here or create some other scheme for displaying news in this context.  Kirby should weigh in on this
//KIRBY:  Are we going to create a whole new scheme for doing the news or just implement the news component in the news page and gussy it up so it looks more like a thing?  What are your thoughts on this?  -B
import React, {Component} from "react";
import NavBar from "../components/navbar.jsx";
import ErrorBoundary from "../components/errorboundary.jsx";


class News extends React.Component {
    render() {
        return(
            <div>
              <NavBar/>
              <h1>NEWS GOES HERE</h1>
            </div>
        );
    }
}

export default News;
