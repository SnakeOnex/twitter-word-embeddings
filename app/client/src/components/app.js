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

  render() {
	let rndr = "nothing";
	if (this.state.embs.words != null) {
	  rndr = "similar";
	  if (this.state.embs.X.length > 1)
		rndr = "plot";
	}
	return (
	  <div className="container">
		<h2>Enter a word</h2>
		<div className="row word-search-wrapper">
		  <WordSearch getEmbs={this.getEmbs} />
		</div>
		<div className="row">
		  {rndr == "similar" || rndr == "plot" ? <EmbeddingTable embs={this.state.embs.words} /> : null }
		</div>
		{rndr == "plot" ? this.getPlot() : null}
	  </div>
	);
  }
}

export default App;
