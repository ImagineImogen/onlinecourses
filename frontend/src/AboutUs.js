import React, { Component, Fragment	} from 'react';
import AppbarMui from './components/AppbarMui';
import HeaderMui from './components/HeaderMui';
import Footer from './components/Footer'
import { withStyles } from '@material-ui/core/styles'
import theme from './theme.js'
import Button from '@material-ui/core/Button'
import FormLabel from '@material-ui/core/FormLabel';
import { TextField } from '@material-ui/core';


const useStyles = theme => ({
  margin: {
    margin: theme.spacing(1),
  },

  FrmLabel: {
    color:"red",
    display: "block",
    alignItems: "center",
    paddingTop: theme.spacing(3),
    paddingBottom: theme.spacing(2),
    marginLeft: theme.spacing(1),

    
  },
  inputField: {
    paddingBottom: theme.spacing(1),
    alignSelf: 'center',
  },

  Btn: {
    margin: theme.spacing(1),
  }

});


class AboutUs extends Component {
 	constructor(props) {
  		super(props);
    	this.state  = {
		    formInfo: {
				email: '',
				question : ''
			}	
		};
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
    }	

    handleChange(event) {
        let formVal = {
        	...this.state.formInfo,
        	[event.target.name]: event.target.value
        };

        this.setState({formInfo: formVal});

  	};

    handleSubmit(event) {
    	event.preventDefault();
		fetch(`${process.env.REACT_APP_API_URL}/api/aboutus`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(this.state.formInfo)
            }
		).then( resp => console.log(resp))
		.then( res => {})
		.catch( error => console.log(error));
    }

  

  render() {
    const { classes } = this.props;
    return (
    	<Fragment >
    	<AppbarMui />
      <HeaderMui />
      <form>
      <div style={{ display: 'inline-flex' }}>
        <div>
        <FormLabel className={classes.FrmLabel}>
          Email Adress:
          </FormLabel>
          </div>
          <div style={{ alignSelf: 'center' }}> 
          <TextField id="outlined-basic" label="Provide an email" variant="outlined" size="small" className={classes.inputField} type="text" name="email" value={this.state.email} onChange={this.handleChange} />
        </div>
        </div>
        
        <FormLabel className={classes.FrmLabel}>
        Your Question:
        <TextField  label="Type in your question" variant="outlined" size="small" className={classes.inputField} value={this.state.value} name="question" onChange={this.handleChange}
          id="outlined-basic"
           />
        </FormLabel>
        
        <Button className={classes.Btn} variant="contained" color="primary" 
		        onClick = {this.handleSubmit}
		        >
         	Submit Your Question
        </Button>
    
      </form>
      <Footer />
      </Fragment>
    );
  }
}
export default withStyles(useStyles) (AboutUs);