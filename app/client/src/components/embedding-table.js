import React from "react";

class EmbeddingTable extends React.Component {
  
  render() {
	console.log(this.props);

	return (
	<table className="embedding-table table col-sm-5">
	  <thead>
		<tr>
		  <th scope="col">Word</th>
		  <th scope="col">Similarity</th>
		</tr>
	  </thead>
	  <tbody>
		  {this.props.embs.map((row) => {
			return (
			  <tr key={row[0]}>
				<td> {row[0]} </td> 
				<td> {row[1]} </td> 
			  </tr>
			);
		  }
		  )}
	  </tbody>
	</table>
	)
  }
}
export default EmbeddingTable;
