//import dependencies
import React, { Component } from 'react';
import './App.css';

import axios from "axios";

//import redux components
import { Provider } from "react-redux";
import store from "./store";

//import chat components
import Chat from "./components/chat/Chat"




//libraries for chatbot UI
import { Widget, addResponseMessage, addLinkSnippet, addUserMessage } from 'react-chat-widget';

import 'react-chat-widget/lib/styles.css';

//import logo from './logo.svg';




//connect redux to application
/*
const App = () => {

	
  return (

	/*chat components goes here 
    <Provider store={store}>
      <div className="container">
      
        {/* Insert Chat Component HERE! }
        <Chat />
      </div>
    </Provider>
  );
}

export default App;
*/

class App extends Component {
  componentDidMount() {
    addResponseMessage("Hello, Welcome to DEMO University..! I am BotBreezy.. Ask me anything about DEMO University.");
  }
  



//send message to the bot -API call

handleNewUserMessage = (message) => {
  console.log(message);
  
  const utterance = message


    axios.post(`botbreezy`, { utterance })
      .then(res => {
        //console.log(res);
       console.log(res.data.fun_res.content);
       addResponseMessage(res.data.fun_res.content)
      })
  
  
};


    
    
    
    
    
 
 

  render() {
    return (
      <div className="App">
        <Widget
          handleNewUserMessage={this.handleNewUserMessage}
          //profileAvatar={logo}
          title="BotBreezy"
          subtitle=""
        />
      </div>
    );
  } 
}
export default App;
