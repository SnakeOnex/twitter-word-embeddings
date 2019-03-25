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
	console.log(this.state.embs);
	return (
	  <div className="container">
		<div className="row">
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
