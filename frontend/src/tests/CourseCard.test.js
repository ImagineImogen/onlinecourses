import React from 'react';
import ReactDom from 'react-dom';
import  CourseCard  from '../components/CourseCard.js';
import { create } from "react-test-renderer"
//import { render } from '@testing-library/react'
import ShallowRenderer from 'react-test-renderer/shallow';
import { BrowserRouter} from 'react-router-dom';


describe("CourseCard component", () => {
    let title = "Test title"
    let description = "Test description"
    let image = "link/to/image.jpg"
    let id = 1

    test("first test", () => {
        const component = create(<BrowserRouter><CourseCard  title = {title}/></BrowserRouter>)
    })
})