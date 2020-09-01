import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import theme from '../theme.js'
import {Link } from 'react-router-dom';

const useStyles = makeStyles({
  root: {
    maxWidth: 345,
    padding: theme.spacing(3),
    height: '40vw',
    marginLeft: theme.spacing(5)

  },
  media: {
    height: 200,
  },
  description: {

  },
});

function CourseCard({title, image, description, id}) {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          component="img"
          image={image}
          title={title}
          
        />
        <CardContent>
          <Typography data-testid = "title" className={classes.title}  gutterBottom variant="h5" component="h2">
            {title || "Unknown"}
            </Typography>
          <Typography className={classes.description} variant="body2" color="textSecondary" component="p">
           {description || "Unknown"}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button variant="outlined" size="small" color="primary" to={`/api/${id}`} component={Link}>
          Click here to find out more
        </Button>
      </CardActions>
    </Card>
  );
}
export default CourseCard;