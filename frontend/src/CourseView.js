import React, {Component} from 'react';
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import CardMedia from '@material-ui/core/CardMedia'
import Button from '@material-ui/core/Button'
import Typography from '@material-ui/core/Typography'
import AppbarMui from './components/AppbarMui'
import {Link } from 'react-router-dom';
import { withCookies, Cookies } from 'react-cookie'



class CourseView extends Component { 

    state = {
        oneCourse: [],
        teacher: [], 
        lessons: []
        
    };

    componentDidMount() {
    fetch(`${process.env.REACT_APP_API_URL}${window.location.pathname}`)
        .then(res => res.json())
        .then((data) => {
            this.setState({ oneCourse: data, teacher: data.teacher.map(tea => (tea.teacher_name))[0], lessons: data.lessons.map(less => (less.description))[0]})
        })
        .catch(error => console.log)

}


enroll = event => {
    let cookieValue = (document.cookie.match(/^(?:.*;)?\s*apitoken\s*=\s*([^;]+)(?:.*)?$/)||[,null])[1]
    if (cookieValue.length > 0) {
        	fetch(`${process.env.REACT_APP_API_URL}${window.location.pathname}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 
                            'Authorization': `Token ${cookieValue}`},
                body: JSON.stringify(this.props.cookie)
                }).then( resp => resp.json())
                .then( res => {
                    alert (res)
                })
                .catch( error => console.log(error))}
    else {
        alert ('An Error occurred!')
    }}


  render () {
    return(
        <div>
          <AppbarMui />
                <Card>
                    <CardMedia style={{height: 300}}
                    component="img"
                        image="../img/room.jpg"
                        />
                    <CardContent>
                        <Typography gutterBottom variant="headline" component="h2" color="secondary">
                            {this.state.oneCourse.title}
                        </Typography>
                        <Typography component="p">
                            {this.state.oneCourse.description}
                        </Typography>
                        <h4>Teacher</h4>
                        <Typography>
                        Teacher is {this.state.teacher || "To be determined"}
                        </Typography>
                        <h4>Lessons</h4>
                         <Typography>
                        {this.state.lessons || "To be continued"}
                        </Typography>
                    </CardContent>
                    <CardActions>
                        <Button size="small" color="secondary" target="_blank" onClick={this.enroll}>
                            Enroll on Course
                        </Button> 
                        
                    </CardActions>
                </Card>
         
        </div>
   ) 
}

}
export default withCookies (CourseView)



