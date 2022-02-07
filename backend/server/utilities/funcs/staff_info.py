from flask import session
def staff_info(utterance,mycursor):
	try:
		#db query for staff info
		#print('session is :',session['ses_validate'])
		
		mycursor.execute("SELECT * FROM staff_info") 
		myresult = mycursor.fetchall()
		
		response = {'fun_res':{
			'is_completed':True,
			'content':myresult[0][1],
			'is_option':False,
			'is_entity':False,
			'options':None,
			'entities':None}
		}
	except :
		print('staff info querry not success...Internal server ERROR in fun staff_info')
		response = {'fun_res':{
			'is_completed':False,
			'content':None,
			'is_option':False,
			'is_entity':False,
			'options':None,
			'entities':None}
		}
	return response
