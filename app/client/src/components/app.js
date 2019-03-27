import React from "react";
import WordSearch from "./word-search";
import EmbeddingTable from "./embedding-table";

class App extends React.Component {
  state = {
	embs: []
  }

  getEmbs = embs => {
	this.setState({
	  embs: embs
	});
  }

  render() {
	return (
	  <div className="container">
		<h2>Enter a word</h2>
		<div className="row word-search-wrapper">
		  <WordSearch getEmbs={this.getEmbs} />
		</div>
		<div className="row">
		  <EmbeddingTable embs={this.state.embs} />
		</div>
	  </div>
	);
  }
}

export default App;
