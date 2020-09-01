import React from 'react';

import { Courses } from  '../Courses.js'

import ReactDom from 'react-dom';
import { create } from "react-test-renderer"
import { BrowserRouter} from 'react-router-dom';


describe("Courses page", () => {
    let data = [
        {id: 1, title: "Potion-Making - Beginner's course", image: "./img/potions.jpg", description: "This highly-rated online course will guide you step-by-step through the composition of your first potion and other related aspects of potion-making"},
        {id: 2, title: "Spells - From Zero to Hero", image: "./img/spells.jpg", description: "An all-comprising course suitable for the people who just took their wands for the first time. Be ready for the fascinating journey into the witchcraft world featuring the most commonly used spells to make your life much easy!"},
        {id: 3, title: "Magical Beasts - Introductory course", image: "./img/beasts.jpg", description: "Step into the marvellous world of powerful creatures and avoid being killed!"}
      ]

    test("CourseView test", () => {
        const component = create(<BrowserRouter><Courses  coursesAPI = {data}/></BrowserRouter>)
        const root = component.root;
        let span = root.findByType("span");
        expect(span.children[0]).toBe("Potion-Making - Beginner's course");
    })
})

