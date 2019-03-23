import React from 'react';

class WordSearch extends React.Component {
  render() {
	return (
	  <form className="word-search">
		<h2>Enter a word</h2>
		<input type="text" required placeholder="some word" />
		<button type="submit">Find similar</button>
	  </form>
	);
  }
}

export default WordSearch;
