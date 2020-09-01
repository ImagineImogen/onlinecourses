import React, { Component } from 'react';
import { withCookies } from 'react-cookie'

class Login extends Component {
	
	state = {
		credentials: {
			username: '',
			password: ''
		},
		isLoginView: true
	}
	inputChanged = event => {
        let cred = this.state.credentials;
        cred[event.target.name] = event.target.value;
        this.setState({credentials: cred});
	}
    login = event => {
    	if (this.state.isLoginView) {
    		fetch(`${process.env.REACT_APP_API_URL}/users/login/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify(this.state.credentials)
                }).then( resp => resp.json())
    			.then( res => {
                    console.log(res.token);
                    this.props.cookies.set('apitoken', res.token);
                    window.location.href = "/";
                })
                .catch( error => console.log(error))
    	}else {
    		fetch(`${process.env.REACT_APP_API_URL}/api/users/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify(this.state.credentials)
                }).then( resp => resp.json())
    			.then( res => {
                    this.setState({isLoginView: true});
                })
                .catch( error => console.log(error))
    	}

    	
    }

    toggleView = () => {
    	this.setState({isLoginView: !this.state.isLoginView});
    }
	render() {
		return <div className="login-container">
		<h1>
			{this.state.isLoginView ? 'Login' : 'Register'}
		</h1>
			<span>Username</span><br/>
			<input style={{marginTop: 5}} type="text" name="username" value={this.state.credentials.username} 
			onChange={this.inputChanged}/><br/>
			<span >Password</span><br/>
			<input style={{marginTop: 5}} type="text" name="password" value={this.state.credentials.password} 
			onChange={this.inputChanged}/><br/>
			 <button style={{marginTop: 10}}onClick={this.login}>
			 {this.state.isLoginView ? 'Login' : 'Register'}
            </button>
            <p style={{marginTop: 10}} onClick={this.toggleView}>
            {this.state.isLoginView ? 'Create Account' : 'Back to login'}
            </p>
		</div>
	}

}

export default withCookies (Login);