import React, { useState } from "react";
import { connect } from "react-redux";


//  Import action
import { userMessage ,sendMessage} from "../../actions/breezy";


const Chat = ({ chat, userMessage, sendMessage}) => {
	//Handle users message
	const [message, setMessage]=useState("");
	

  //  Function that handles user submission
  const handleClick = async (e) => {
    const code = e.keyCode || e.which;

    if (code === 13) {
      console.log(message);
      userMessage(message);
      sendMessage(message);
      setMessage("");
    }};
	
	return(
		<div className='chat'>
			<h1>BotBreezy</h1>
			
			{/*Handle messages*/}
			
			{chat.length === 0 ? "": chat.map((msg) => <div className={msg.type}>{msg.message}</div>)}
			
			{/*Input box*/}
			<input id="chatBox"
				onChange={(e) => setMessage(e.target.value)}
				onKeyPress={handleClick}
				value={message}>
			</input>
		</div>
		
		)
	
	}
	
const mapStateToProps = (state) => ({
  chat: state.breezy.messages,
});
	
export default connect(mapStateToProps, { userMessage ,sendMessage})(Chat);

