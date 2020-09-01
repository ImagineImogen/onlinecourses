import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Courses from './Courses';
import Login from './login'
import AboutUs from './AboutUs'
import { MuiThemeProvider, CssBaseline } from '@material-ui/core';
import theme from "./theme";
import { BrowserRouter, Route, Switch} from 'react-router-dom';
import { CookiesProvider } from 'react-cookie'
//import Login_hooks from "./Login_hooks"
import CourseView from './CourseView';

const routing = (
	<BrowserRouter>
		<CookiesProvider>
		<MuiThemeProvider theme={theme}>
		<CssBaseline />
		<Switch>
			<Route exact path="/" component={App}></Route>
			<Route exact path="/courses" component={Courses}></Route>
			<Route path="/teachers">Teachers</Route>
			<Route exact path="/login" component={Login}></Route>
			<Route exact path="/api/:id" component={CourseView}></Route>
			<Route exact path="/aboutus" component={AboutUs}></Route>
			</Switch>
			</MuiThemeProvider>
		</CookiesProvider>
	</BrowserRouter>
)

ReactDOM.render(
  routing, document.getElementById('root')
);

