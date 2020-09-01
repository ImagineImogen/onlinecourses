import React from 'react';
import * as ReactDOM from 'react-dom';
import  App  from '../App.js';
import renderer from 'react-test-renderer'
import { BrowserRouter} from 'react-router-dom';
import { render, fireEvent, getByTestId } from '@testing-library/react'


test("App rendering", ()=> {
    const root = document.createElement("div");
    ReactDOM.render(<BrowserRouter><App /></BrowserRouter>, root)

    expect(root.querySelector('h2').textContent).toBe("Hogwarts Online");
})

test("user goes to Courses page", () => {
    const { getByTestId} = render(<BrowserRouter><App/ ></BrowserRouter>);

    fireEvent.click(getByTestId("btnCourses"))
    

})