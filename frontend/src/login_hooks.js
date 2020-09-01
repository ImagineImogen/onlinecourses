import React, { useState, useEffect } from 'react';

export default function Login_hooks(){
	const [username, setUsername] = useState("")
	const [password, setPassword]  = useState("")
	const [email, setEmail] = useState("")
	const [isSubmitting, setisSubmitting] = useState(false)
	//const [{response, isLoading, error}}, doFetch] = useFetch('someurl')

	const handleSubmit = event=> {
		event.preventDefault()
		setisSubmitting = true
		const userData = {

		}
	}

	useEffect(() => {
		if (!isSubmitting){
			return
		}
		fetch(`${process.env.REACT_APP_API_URL}/users/login/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify(this.state.credentials)
                }).then( resp => resp.json())
    			.then( res => {
                    console.log(res.token);
                    setisSubmitting(false)
                    this.props.cookies.set('apitoken', res.token);
                    window.location.href = "/";
                })
                .catch( error => console.log(error))
                setisSubmitting(false)
	}

		)
	return(
		<div

		style={{
			textAlign: 'center'
		}}>
			<h2>Login</h2>
			<form
			style={{
				display: 'grid',
				alignItems: 'center',
				justifyItems: 'center'
			}}
			onSubmit={handleSubmit}>
			<input 
			type="text" 
			placeholder="Username"
			onChange={event => setUsername(event.target.value)}
			/>
			<input 
			type="email" 
			placeholder="email"
			value={email}
			onChange={event => setEmail(e.target.value)}
			/>
			<input type="password"
			 placeholder="password"
			 onChange={event => setPassword(event.target.value)}
			 />
			<button type="submit" disabled={isSubmitting}>Submit</button>
			</form>

		</div>
		)
}
