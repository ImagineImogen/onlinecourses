import React, { Component } from 'react';
import './App.css';
import styled from 'styled-components';
import { Grid, useMediaQuery, Hidden, Box, Button } from "@material-ui/core";

import AppbarMui from './components/AppbarMui';
import HeaderMui from './components/HeaderMui';
import CourseCard from './components/CourseCard';
import Footer from './components/Footer'
import theme from './theme.js'
import {Link } from 'react-router-dom';
import { withCookies } from 'react-cookie'


const data = [
  {id: 1, title: "Potion-Making - Beginner's course", image: "./img/potions.jpg", description: "This highly-rated online course will guide you step-by-step through the composition of your first potion and other related aspects of potion-making"},
  {id: 2, title: "Spells - From Zero to Hero", image: "./img/spells.jpg", description: "An all-comprising course suitable for the people who just took their wands for the first time. Be ready for the fascinating journey into the witchcraft world featuring the most commonly used spells to make your life much easy!"},
  {id: 3, title: "Magical Beasts - Introductory course", image: "./img/beasts.jpg", description: "Step into the marvellous world of powerful creatures and avoid being killed!"}
]

class App extends Component{

    render (){

    return (
        <>
      <Hidden only="xs">
        <AppbarMui />
      </Hidden>
      <Grid container spacing={3} justify="center">
        <Grid
          item
          xs={12}
          md={7}
          lg={12}
        >
        <HeaderMui />
        <h2 style={{paddingTop: 20, paddingBottom: 20, marginLeft: 80}}> Most Popular Courses</h2>
        <Box p={(2, 4)}>
            <Grid container justify="flex-start" spacing={2} direction="row" alignItems="flex-start">
                {data.map((card) => (
                    <Grid key={card.id} item xs={4}>
                         <CourseCard
                            title={card.title}
                            image={card.image}
                            description={card.description}
                        /> 
                    </Grid>
                ))}
            </Grid>
        </Box>
        <Button  data-testid = "btnCourses" variant="contained" color="primary" to='/courses' component={Link} style={{ marginTop: "auto",  marginBottom: "auto", marginLeft: theme.spacing(9)}}> All Courses >></Button>
        <Footer />
        </Grid>
      </Grid>
    </>
  );
}
}

export default App;
