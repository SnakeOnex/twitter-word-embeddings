import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import WordSearch from "./word-search.js";

const Router = () => (
  <BrowserRouter>
	<Switch>
	  <Route exact path="/" component={WordSearch} />
	  <Route component={WordSearch} />
	</Switch>
  </BrowserRouter>
)

export default Router;
