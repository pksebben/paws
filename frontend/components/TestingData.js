/*
Testing Data
This is basically lorem ipsum to test modules out until we have some form
of storage.
TODO:Implement storage and deprecate this module.
*/



const eventdata = {
    title: "Lemon Party",
    eventImage: "I'm gonna grow up to be an image!", //TODO: replace with actual image data
    eventDesc: "And then we hauled it, we called a couple of friends, and there was about twelve of us, and we hauled it down to the beach and we soaked it with gasoline, because we didn't know any better at that time. And... because gasoline as you know... we use diesel now, gasoline's very volatile, and when it flamed up, it was like a second sun brought down to this earth, it was just... it transfixed us, but... that's where the story begins, in fact.",
    shelterLink: "https://photricity.com/flw/ajax/",
    shelterName: "big bob's discount kill-free dog dorm",
    date: "1/13/59"
}

const newsdata = {
    title: "Invasion of the space cats!",
    snippet: "Brooklyn is under attack!  This afternoon at 5:45 Zulu time, space cats on hipster's tights all over the borough came alive and began attacking people.  It is yet unknown what phenomenamena caused the feline invasion, but residents are advised to stay inside or report to the nearest emergency shelter or water feature.  The police have begun to implement a strategy to deal with the furry terrors, shipping emergency stores of catnip from all across the country.  People are strongly advised to avoid canal street in chinatown and sushi restaurants.",
    link:" https://www.youtube.com/watch?v=wZZ7oFKsKzY"
};

const analyticsdata = {
    amountRaised: 9000,
    numGamers: 5,
    numDonors: "like, a bajillion",
    numShelters: "zero. So sad."
}

const recentgamerdata = {
    name: "Nyan Cat",
    joinDate: "4/20/duuuuude."
}

const recentshelterdata = {
    name: "Captain art school's freegan dog shelter",
    joinDate: "like, whenever, dude",
    events: "we don't care."
}

const topgamersdata ={
    name: "Snake Pisskin",
    raised: "all the money",
    shelters: "Shelters go here.  Need to make it dynamic and pull from a dict",
    events: "events go here.  Make it dynamic",
    achievements: "He hath achieved NOTHING!"
}



export {eventdata, newsdata, analyticsdata, recentgamerdata, recentshelterdata, topgamersdata };
