from flask import session
def greetings(utterance,mycursor,db_connection):
	
	
	
	response = {'fun_res':{
		'is_completed':True,
		'content':'I am here to provide information about Demo University.. tell me how can I help you?',
		'is_option':False,
		'is_entity':False,
		'options':None,
		'entities':None}
	}

	return response
