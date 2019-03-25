import React from 'react';
import axios from 'axios';

class WordSearch extends React.Component {

  constructor() {
	super();

    this.handleClick = this.handleClick.bind(this)
  }

  handleClick () {
	axios.get('http://194.182.80.90:5000/nigger')
	    .then(response => console.log(response))
  }


  render() {
	return (
	  <div className="container">
		<form className="word-search">
		  <h2>Enter a word</h2>
		  <input type="text" required placeholder="some word" />
		  <button type="submit" onClick={this.handleClick}>Find similar</button>
		</form>
	  </div>
	);
  }
}

export default WordSearch;
