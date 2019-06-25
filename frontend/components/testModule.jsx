//This is a module for testing Redux.  Once there is better implenentation of redux on the site, delete it.
//NOTE: this only takes data and displays it.  testInput will input data.
//this is to keep me from confusing shit.

import React from 'react';
import { connect } from 'react-redux';

//this takes store data and makes it available to the component
const mapStateToProps = state => {
    //this return grants the component a value keyed to 'fhqwhgads' from 'state.fhqwhgads'
    return { fhqwhgads: state.fhqwhgads };
};

//This uses the deconstruction syntax "{ fhqwhgads }" to extract whatever is keyed to 'fhqwhgads' from
//the object that is passed in.
//  When passed, the .map f() will attempt to extract .id and .title from each element of the list 'fhqwhgads'
//  THIS MEANS that the payloads to the reducer for fhqwhgads must contain an ID and a title key.
//this is accomplished in the action creator
const ThisModule = ({ fhqwhgads }) => (
    <ul>
      { fhqwhgads.map(el => (
          <li key={el.id}>
            {el.title}
          </li>
      ))}
    </ul>
);

const TestModule = connect(mapStateToProps)(ThisModule);

export default TestModule;
