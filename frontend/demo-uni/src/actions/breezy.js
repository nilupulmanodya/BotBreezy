//import types
import {INPUT_SUCCESS,INPUT_FAIL,MESSAGE_SUCCESS,MESSAGE_FAIL} from './types'


//  Import axios
import axios from "axios";

//  Function that handles  users message
export const userMessage = (message) => async (dispatch) => {
  try {
    dispatch({ type: INPUT_SUCCESS, payload: message });
  } catch (err) {
    dispatch({ type: INPUT_FAIL });
  }
};


//create a session API call
//--------------


//send message to the bot -API call

export const sendMessage = (message) => async (dispatch) => {
  try {
    const body = { utterance: message };
    const res = await axios.post("/botbreezy", body);
    
    console.log(res.data.fun_res.content)
    dispatch({
      type: MESSAGE_SUCCESS,
      
      payload: res.data.fun_res.content,
    });
  } catch (err) {
    dispatch({ type: MESSAGE_FAIL });
  }
};
