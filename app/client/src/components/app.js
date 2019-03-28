import React from "react";
import WordSearch from "./word-search";
import EmbeddingTable from "./embedding-table";

class App extends React.Component {
  state = {
	embs: []
  }

  getEmbs = embs => {
	this.setState({
	  embs: embs,
	  plot: {}
	});
  }

  render() {
	console.log(this.state.embs.length == 0);
	console.log(this.state.embs);
	let rndr = "nothing";
	if (this.state.embs.length > 0)
	  rndr = "similar";
	return (
	  <div className="container">
		<h2>Enter a word</h2>
		<div className="row word-search-wrapper">
		  <WordSearch getEmbs={this.getEmbs} />
		</div>
		<div className="row">
		  {rndr == "similar" ? <EmbeddingTable embs={this.state.embs} /> : null }
		</div>
	  </div>
	);
  }
}

export default App;
