import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" style={{ fontSize: 12}}>
      {'Copyright © '}
      <Link color="inherit" href="localhost:3000">
        Hogwarts Online
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({

  footer: {
    padding: theme.spacing(3, 9),
    marginTop: theme.spacing(3),
    backgroundColor:
      theme.palette.type === 'light' ? theme.palette.grey[200] : theme.palette.grey[800],
  },
}));

export default function StickyFooter() {
  const classes = useStyles();

  return (

      <footer className={classes.footer}>
        
          <Typography variant="body1" align="left" style={{ fontSize: 13, fontWeight: "bold"}}>Hogwarts Online</Typography>
          <Typography variant="body1" style={{ fontSize: 12}}>Magical Lane 4</Typography>
          <Typography variant="body1" style={{ fontSize: 12}}>12478 London</Typography>
          <Typography variant="body1" style={{ fontSize: 12}}>United Kingdom</Typography>
          <Copyright />
        
      </footer>
 
  );
}