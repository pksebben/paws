### KIRBYs
| Filename | line # | KIRBY
|:------|:------:|:------
| frontend/app.jsx | 5 | We should talk about how to do static files and such.  This is dependant on my revisiting that part of webpack
| frontend/views/news.jsx | 5 | Are we going to create a whole new scheme for doing the news or just implement the news component in the news page and gussy it up so it looks more like a thing?  What are your thoughts on this?  -B

### BENs
| Filename | line # | BEN
|:------|:------:|:------
| frontend/app.jsx | 6 | ++PRIORITY++ Figure out webpack again so I can advise re: static files
| frontend/components/analytics.jsx | 6 | should we deprecate this module?
| frontend/components/events.jsx | 6 | Add state management
| frontend/components/navbar.jsx | 5 | get rid of all that extra code I put in here to work around the link hiding problem
| frontend/components/navbar.jsx | 10 | is there a way to implement modals without any CSS in order to test modals here?  Would it be easier just to have a little CSS in there?  Look it up.
| frontend/components/news.jsx | 3 | make a design decision about whether to keep this module as-is or to contain more than one item in it (probably, make it simply *the* news module and put all functions in here)
| frontend/components/ourstory.jsx | 2 | this is likely a deprecated module, and an atrefact from when I got all module-fever-crazy.  Make a decision.
| frontend/views/gamerprofile.jsx | 5 | Gamer profile notifications have to be created.  Should they be in their own module for readability or live native in the gamer profile view?

### TODOs
| Filename | line # | TODO
|:------|:------:|:------
| frontend/components/navbar.jsx | 4 | Check out the react-router-redux-whatever and use it so that the component knows what page it's on and doesn't serve up pointless lynx
| frontend/components/navbar.jsx | 6 | replace spyglass image with the popup for searching
| frontend/components/navbar.jsx | 8 | Replace the 'Home' Link with the Paws logo
| frontend/components/navbar.jsx | 9 | Strike the 'gamerprofile' and 'shelterprofile' lynx and have those implemented via the SIGN IN / UP button.
| frontend/components/testingdata.js | 5 | Implement storage and deprecate this module.
| frontend/redux/actions/index.js | 2 | Refactor all redux to use ducks patterning
| frontend/redux/index.js | 2 | once redux is integrated properly, delete this file.
| frontend/redux/reducers/index.js | 13 | fix this switch case and test it
| frontend/views/gamerprofile.jsx | 4 | Craft out this page according to Kirby's spec
| frontend/views/gamerprofile.jsx | 6 | Do we want to make the 'upcoming fundraiser' a link to that fundraiser?
| frontend/views/home.jsx | 3 | Refactor this page into it's component modules
| frontend/views/news.jsx | 4 | Fix up the news component and figure out a way to either use it here or create some other scheme for displaying news in this context.  Kirby should weigh in on this
| frontend/views/shelterprofile.jsx | 1 | fill out shelter profile according to Kirby's spec

### IANs
| Filename | line # | IAN
|:------|:------:|:------
| frontend/components/navbar.jsx | 7 | potentially we might replace SIGN IN / UP with a modular, as well as DONATE.  What do you think? - ben

### GOOGLEs
| Filename | line # | GOOGLE
|:------|:------:|:------
| frontend/redux/reducers/index.js | 2 | what directory structures are used in redux?  Can we split the reducers / actions / etc into multiple files?  What would that look like?
| frontend/redux/reducers/index.js | 3 | redux pro move - RTFM - js Object.assign().
| frontend/redux/reducers/index.js | 4 | redux pro move - RTFM - js concat() slice() ...spread
| frontend/redux/reducers/index.js | 5 | redux pro move - redux combineReducers()