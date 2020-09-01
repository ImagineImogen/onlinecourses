import React from 'react';
import ReactDom from 'react-dom';
import  Footer  from '../components/Footer.js';
import renderer from 'react-test-renderer'


it("Footer rendering", ()=> {
    const div = document.createElement("div");
    ReactDom.render(<Footer />, div)
})

it("matches snapshot", () => {
    const tree = renderer.create(<Footer />).toJSON();
    expect(tree).toMatchSnapshot()
})