import React, { Component } from 'react';
import './App.css';
import Toggle from './Profile/Togglebutton';
import Togglebutton from './Profile/Togglebutton';
import Flashcard from './Profile/Flashcard';
import Flashcard2 from './Profile/Flashcard2';
import Flashcard3 from './Profile/Flashcard3';
import FlashcardData from './Profile/FlashcardData';

class App extends Component {

  render() {
    return(
      <div className ="App">
          <Flashcard />
          <Flashcard2 />
          <Flashcard3 />
        </div>
    );
  }
}

export default App;