### TODOs
| Filename | line # | TODO
|:------|:------:|:------
| frontend/components/homeLeaderboard.jsx | 1 | implement some form of multiplying this in the same manner that Kirby's PHP did.
| frontend/components/navbar.jsx | 4 | Check out the react-router-redux-whatever and use it so that the component knows what page it's on and doesn't serve up pointless lynx
| frontend/components/navbar.jsx | 6 | replace spyglass image with the popup for searching
| frontend/components/navbar.jsx | 8 | Replace the 'Home' Link with the Paws logo
| frontend/components/navbar.jsx | 9 | Strike the 'gamerprofile' and 'shelterprofile' lynx and have those implemented via the SIGN IN / UP button.
| frontend/components/testingdata.js | 5 | Implement storage and deprecate this module.
| frontend/views/gamerprofile.jsx | 4 | Craft out this page according to Kirby's spec
| frontend/views/gamerprofile.jsx | 6 | Do we want to make the 'upcoming fundraiser' a link to that fundraiser?
| frontend/views/home.jsx | 3 | Refactor this page into it's component modules
| frontend/views/shelterprofile.jsx | 1 | fill out shelter profile according to Kirby's spec

### BENs
| Filename | line # | BEN
|:------|:------:|:------
| frontend/components/navbar.jsx | 5 | get rid of all that extra code I put in here to work around the link hiding problem
| frontend/components/navbar.jsx | 10 | is there a way to implement modals without any CSS in order to test modals here?  Would it be easier just to have a little CSS in there?  Look it up.
| frontend/components/news.jsx | 3 | make a design decision about whether to keep this module as-is or to contain more than one item in it (probably, make it simply *the* news module and put all functions in here)
| frontend/components/ourstory.jsx | 2 | this is likely a deprecated module, and an atrefact from when I got all module-fever-crazy.  Make a decision.
| frontend/views/gamerprofile.jsx | 5 | Gamer profile notifications have to be created.  Should they be in their own module for readability or live native in the gamer profile view?

### IANs
| Filename | line # | IAN
|:------|:------:|:------
| frontend/components/navbar.jsx | 7 | potentially we might replace SIGN IN / UP with a modular, as well as DONATE.  What do you think? - ben