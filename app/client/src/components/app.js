import React from "react";
import WordSearch from "./word-search";
import EmbeddingTable from "./embedding-table";
import Plot from "react-plotly.js";

class App extends React.Component {
  state = {
	embs: {}
  }

  getEmbs = embs => {
	this.setState({
	  embs: embs,
	});
  }

  getPlot() {
	return (
		<Plot
        data={[
          {
			x: this.state.embs.X.map(x => { return parseFloat(x)}),
			y: this.state.embs.Y.map(y => { return parseFloat(y)}),
            type: 'scatter',
			mode: 'markers+text',
			text: this.state.embs.labels,
			textposition: 'bottom-center',
            marker: {color: 'red'},
          },
        ]}
        layout={{xaxis: { range: [-50, 50]}, yaxis: { range: [-50, 50]}, width: 640, height: 480, title: 'Plotted words'} }
      />
	);
  }

  getError() {
	const err = this.state.embs.err;
	return (
	  <div className="alert alert-danger" style={{"margin": "0 auto"}} role="alert">
	    Word {err[0]} has not been found!
	  </div>
	);
  }

  render() {
	let embs = this.state.embs;
	console.log(embs);
	let similar = false;
	let error = false;
	let plot = false;

	if (Object.entries(embs).length !== 0 && embs.constructor === Object) {
	  console.log("NFDSF")
      if (embs.err.length == 0) {
		similar = true;
		console.log("ASDF");
	  } else if (embs.err.length != 0) {
		error = true;
	  }
	  if (this.state.embs.X.length > 1)
		plot = true;
	}
	return (
	  <div className="container">
		<h2>Enter a word</h2>
		<div className="row word-search-wrapper">
		  <WordSearch getEmbs={this.getEmbs} />
		</div>
		<div className="row">
		  {similar ? <EmbeddingTable embs={this.state.embs.words} /> : null }
		  {error ? this.getError() : null }
		</div>
		{plot ? this.getPlot() : null}
	  </div>
	);
  }
}

export default App;
