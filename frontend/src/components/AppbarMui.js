import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import {Link } from 'react-router-dom';
import { withRouter } from 'react-router-dom';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },

  title: {
    flexGrow: 1,
  },
tabRoot: {
    "&:hover": {
      color: "purple",
      opacity: 2,
    },
    "&$tabSelected": {
      color: "violett",
    },
    "&:focus": {
      color: "red",
      outline: 'none'
    }
  },

}));



function AppbarMui(props)  {
  const classes = useStyles();

  return (

    <div className={classes.root}>
      <AppBar position="static" color="transparent" style={{ boxShadow: 'none'}}>
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Welcome to Hogwarts Online
          </Typography>
          <Tabs value={props.location.pathname}>
            <Tab classes={{ root: classes.tabRoot, selected: classes.tabSelected }} value='/' label='Home' to='/' component={Link} />
            <Tab classes={{ root: classes.tabRoot, selected: classes.tabSelected }} value='/courses' label='Courses' to='/courses' component={Link} />
            <Tab classes={{ root: classes.tabRoot, selected: classes.tabSelected }} value='/aboutus' label="About Us" to='/aboutus' component={Link} />
          </Tabs>
          <Button color="inherit" to='/login' component={Link}>Login</Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default withRouter(AppbarMui);
