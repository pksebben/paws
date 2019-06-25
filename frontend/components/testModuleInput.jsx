//this is a second module for testing Redux.  It provides input for the other module

import React from 'react';
import { connect } from 'react-redux';
import uuidv1 from 'uuid';
import { addFhqwhgads } from'../redux/actions/index';

//this is where I get confused.  
function mapDispatchToProps(dispatch) {
    return {
        addFhqwhgads : fhqwhgads => dispatch(addFhqwhgads(fhqwhgads))
    };
}

class TestInput extends React.Component {
    constructor(){
        super();
        this.state = {
            title:""
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    //the way this is constructed, all changes modify the text in the state (cont'd on next f())
    handleChange(event){
        this.setState({ [event.target.id]: event.target.value });
    }

    //...and are loaded into the store on pressing the 'submit' button
    handleSubmit(event){
        event.preventDefault();
        const { title } = this.state;
        const id = uuidv1();
        this.props.addFhqwhgads({ title, id });
        this.setState({ title: "" });
    }

    render() {
        //GOOGLE: why are we pulling {title} from state?
        const { title } = this.state;
        return( 
            <form onSubmit={this.handleSubmit}>
              <div className="form-group">
                <label htmlFor="title">Title</label>
                <input
                  type="text"
                  className="form-control"
                  id="title"
                  value={title}
                  onChange={this.handleChange}
                />
              </div>
              <button type="submit" className="btn btn-success btn-lg">SAVE</button>
            </form>
            
        );
    }
}

const FhqwhgadsInput = connect(null, mapDispatchToProps)(TestInput);

export default FhqwhgadsInput;
