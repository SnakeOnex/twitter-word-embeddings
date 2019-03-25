import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import App from "./app.js";

const Router = () => (
  <BrowserRouter>
	<Switch>
	  <Route exact path="/" component={App} />
	  <Route component={App} />
	</Switch>
  </BrowserRouter>
)

export default Router;
