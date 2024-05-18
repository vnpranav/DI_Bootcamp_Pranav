import React from "react";

class StarWars extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            name : "",
            birth_year : 0,
            gender : "",
            eye_color : "",
        };
    }

    componentDidMount(){
        let number = Math.floor(Math.random() * 83 + 1)
        let url = "https://swapi.dev/api/people/" + number + "/"

        fetch(url).then((resp) => resp.json()).then((resp) => this.setState(
            {
                name : resp.results.name,
                birth_year : resp.results.birth_year,
                gender : resp.results.gender,
                eye_color : resp.results.eye_color,
            }
        ))
    }

    render() {
        let { name, birth_year, gender, eye_color } = this.state
        return (
            <div>
                <h1> {name}</h1>
                <p>Gender : {gender}</p>
                <p>Birth Year : {birth_year}</p>
                <p>Eye Color : {eye_color}</p>
            </div>
        );
    }
}

export default StarWars;