  import React from 'react';
  import './FirstpageStyle.css';
  import Pin from './logo2.png';
  import { withRouter, Link } from "react-router-dom";


  class Firstpage extends React.Component {

  constructor(props){
      super(props);
      this.state = {
          value: '',
          returnedValue: 'default'
        };
        this.handleChange = this.handleChange.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
  }

  onSubmit (event) {
    event.preventDefault();
    var url = 'http://54.153.101.175:8000/user/user_exists/';
    const value = this.state.value;
    fetch(url, {
    method: 'POST',
    headers: {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json'},
	body: JSON.stringify({"email": value})
	})
    .then(response => {return(response.json())})
    .then(response => {this.setState({returnedValue: response["value"]})})
    .then(response => {this.redirectToTarget()})
  }

  handleChange(event) {
      this.setState({value: event.target.value});
    }

  redirectToTarget = () => {
    const value = this.state.value;
    if (this.state.returnedValue === true){
        this.props.history.push({pathname: '/signin', state: {email: value}});
    }
    else {
        this.props.history.push({pathname: '/Signup', state: {email: value}});
    }
  }

  render(){
  return(   <div className="landpage">  
              <div className="topnav">
                  <Link className="active" to="/"><img src={Pin} alt="FigitLogo"/></Link>
                      <div className="topnav-right">
                          <Link to="/help">Help</Link>
                          <Link to="/about">About</Link>
                      </div>
              </div>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <div className="header" id="home">
                  <h2 class="headingp">Analysing Git.</h2>
                  <h2 class="headingp">Simplified.</h2>
              </div>
              <div className="container-fluid">
                  <div className="form-group">  
                      <form action="#" onSubmit={(event)=>{this.onSubmit(event)}}>
                          <div className="d-flex justify-content-center">
                              <input type="email" className="form-control" id="usr" name="username" placeholder="Enter your email here" value={this.state.value} onChange={this.handleChange}></input>
                          </div>
                          <div className="d-flex justify-content-center">
                              <button type="submit" className="getinbutton">Get Started</button>
                          </div>
                          <br/>
                          <div className="d-flex justify-content-center">
                              <Link to={{pathname:"/signin", state:{email: ''}}}>or Sign In</Link>
                          </div>
                      </form>
                  </div>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              <br/>
              </div>
          </div>
       );  
  }
  }

  export default withRouter(Firstpage);