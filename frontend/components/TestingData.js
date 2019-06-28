/*
Testing Data
This is basically lorem ipsum to test modules out until we have some form
of storage.
TODO:Implement storage and deprecate this module.
*/

const eventdata = {
    title: "Professional Event",
    eventImage: "Image will go here", //TODO: replace with actual image data
    eventDesc: "This is a professional event.  Professionals only.  There will be no shenanigans at this event.  Only professional professionals professing professional profession things. Professionals.",
    shelterLink: "https://photricity.com/flw/ajaxhttps://www.gettyimages.com/photos/professional?phrase=professional&sort=best",
    shelterName: "Professional dog shelter.  For professional dogs.",
    date: "1/13/59"
}

const newsdata = {
    title: "Today's professional news",
    snippet: "In professional news today, stocks went up and then down again, and professional businesses did professional work in an incredibly professional manner.  Then, some other business stuff happened.",
    link:"https://www.youtube.com/watch?v=RXJKdh1KZ0w"
};

const analyticsdata = {
    amountRaised: 9000,
    numGamers: 5,
    numDonors: "like, a bajillion",
    numShelters: "zero. So sad."
}

const recentgamerdata = {
    name: "Pro Gamer",
    joinDate: "the date goes here"
}

const recentshelterdata = {
    name: "Pro dog shelter",
    joinDate: "the date goes here, and no funny business",
    events: "this is where the shelter's events go, without tomfoolery"
}

const topgamersdata ={
    name: "Gamer Pro",
    raised: "A sensible amount without humor",
    shelters: "Shelters go here.  Need to make it dynamic and pull from a dict",
    events: "events go here.  Make it dynamic",
    achievements: "This is where the achievements go, if they are professional."
}

export {eventdata, newsdata, analyticsdata, recentgamerdata, recentshelterdata, topgamersdata };
