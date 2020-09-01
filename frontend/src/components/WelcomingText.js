import React, {useEffect, useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';


const useStyles = makeStyles((theme => ({


headerText: {
  fontSize: 17,
  display: 'inline-block',
  alignItems: "center",
  position: "absolute",
  marginTop: 0,
  marginBottom: "auto",
  paddingRight: theme.spacing(10),
  marginLeft: 0,
  marginRight: 20,
  zIndex: 999,
  top: "60%",
  width: "100%",



},




}

	)));

function WelcomingText() {
  const classes = useStyles();

  const [showLoading, setShowLoading] = useState(false)

  useEffect(
        () => {
          let timer1 = setTimeout(() => setShowLoading(true), 1500)

   return () => {
            clearTimeout(timer1)
          }
        },
        [] //useEffect will run only one time
           //if you pass a value to array, like this [data] than clearTimeout will run every time this value changes (useEffect re-run)
    )
  return showLoading && (
    
    <Box component="span" className={classes.headerText} flexWrap="wrap" whiteSpace="wrap">Hogwarts Online is the first platform out there for the wizards far away from Hogwarts. Experience the power of British magical education while still working muggle job. All you need is a magic wand and to be a proved wizard!</Box>
      
  );
}
export default WelcomingText;