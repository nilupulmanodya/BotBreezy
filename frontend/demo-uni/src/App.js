//import dependencies
import React from 'react';
import './App.css';



//import redux components
import { Provider } from "react-redux";
import store from "./store";

//import chat components
import Chat from "./components/chat/Chat"

//connect redux to application

const App = () => {

	
  return (

	/*chat components goes here */
    <Provider store={store}>
      <div className="container">
      
        {/* Insert Chat Component HERE! */}
        <Chat />
      </div>
    </Provider>
  );
}

export default App;
