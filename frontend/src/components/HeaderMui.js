import React, {useEffect, useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import WelcomingText from './WelcomingText'

const url = process.env.PUBLIC_URL  + "/img/castle.jpg";
const useStyles = makeStyles((theme => ({

header: {
	height: "57vh",
  background: `url(${url})`,
  backgroundSize: "cover",
  alignItems: "center",
  justifyContent: "center",
  alignItems: "center",
  backgroundPosition: "center center",
  backgroundAttachment: "fixed",
  flexGrow: 1,
  position: "relative",
  

},


textWrapper: {
  
    display: "block",
    paddingRight: 15,
    paddingLeft: theme.spacing(10),
    paddingBottom: 20,
    alignItems: "center",
    width: "fit-content",
    position: "absolute",
    zIndex: 999,
    top: "50%",
    width: "100%",



    

},



}

	)));

function HeaderMui() {
  const classes = useStyles();

  const [showLoading, setShowLoading] = useState(false)

  useEffect(
        () => {
          let timer1 = setTimeout(() => setShowLoading(true), 1000)

   return () => {
            clearTimeout(timer1)
          }
        },
        [] 
           
    )
  return  (
    <Box className={classes.header} flexWrap="wrap">
    <Box className={classes.textWrapper} width="100%" flexWrap="wrap">
     <h2 >Hogwarts Online</h2>
    <WelcomingText />
    </Box>
    </Box>
  );
}
export default HeaderMui;