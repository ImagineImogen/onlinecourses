import React, { Component} from 'react';
import styled from 'styled-components';

const StyledLink = styled.a`
	color: ${props => props.active ? 'pink' : '#fff'};
	float: left;
    font-size: 16px;
    text-align: center;
    text-decoration: none;
    display: block;
    padding: .5rem 1rem;
    font-weight: 400;
    line-height: 1.5;

	&:hover {
		color: #7cb62f;
		text-decoration: none;
	}
	
`

class Link extends React.Component {
	render() {
		return (
				<StyledLink href={this.props.link}> {this.props.text} </StyledLink>
			)
	}
}
export default Link