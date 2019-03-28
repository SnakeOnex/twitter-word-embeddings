import React from 'react';
import axios from 'axios';

class WordSearch extends React.Component {

  constructor() {
	super();
	this.state = {
	  inputValue: ""
	};

    //this.handleClick = this.handleClick.bind(this)
  }

  myInput = React.createRef();

  handleClick = e => {
	e.preventDefault();
	console.log(e);
	fetch("http://194.182.80.90:5000/" + this.state.inputValue) // Call the fetch function passing the url of the API as a parameter
	.then((response) => response.json())
	.then((responseJSON) => {
	  console.log(responseJSON.embs);
	  this.props.getEmbs(responseJSON);
	})
	.catch(function(error) {
	  console.log(error);
	});
  }


  render() {
	return (
	  <form className="word-search form-group row" onSubmit={this.handleClick} >
		<input 
		  className="form-control col-sm-8"
		  type="text"
		  value={this.state.inputValue}
		  onChange={e => this.updateInputValue(e)}
		  required 
		  placeholder="some word"
		 />
		<button type="submit" className="btn btn-primary col-sm-4">Find similar</button>
	  </form>
	);
  }

  updateInputValue(e) {
	this.setState({
	  inputValue: e.target.value
	});
  }
}

export default WordSearch;
