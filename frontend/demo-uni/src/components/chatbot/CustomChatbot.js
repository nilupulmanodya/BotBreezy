import React from "react";
import ChatBot from "react-simple-chatbot";
import { ThemeProvider } from "styled-components";

function SendToConsole(utterance){
	console.log(utterance);
	}


function CustomChatbot(props) {
  const config = {
    width: "300px",
    height: "400px",
    floating: true
  };

  const theme = {
    background: "white",
    fontFamily: "Arial, Helvetica, sans-serif",
    headerBgColor: "#00B2B2",
    headerFontColor: "#fff",
    headerFontSize: "25px",
    botBubbleColor: "#00B2B2",
    botFontColor: "#fff",
    userBubbleColor: "#fff",
    userFontColor: "#4c4c4c"
  };

  const steps = [
    
    {
		id: '1',
		message: 'Hello World',
		trigger: '2',
	},
	{
		id: '2',
		message: ({ previousValue, steps }) => 'Hello',
		trigger: ({ value, steps }) => '3',
	},
	{
	  id: '3',
	  message: 'Bye',
	  end:true
	  //trigger:'end'
	}

  ];

  return (
    <ThemeProvider theme={theme}>
      <ChatBot steps={steps} {...config} />
    </ThemeProvider>
  );
}

export default CustomChatbot;
