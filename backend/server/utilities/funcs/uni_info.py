from flask import session
def uni_info(utterance,mycursor):
	try:
		#db query for uni_info
		#print('session is :',session['ses_validate'])
		
		mycursor.execute("SELECT * FROM uni_info_des") 
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
		print('uni_info querry not success...Internal server ERROR in fun uni_info')
		response = {'fun_res':{
			'is_completed':False,
			'content':None,
			'is_option':False,
			'is_entity':False,
			'options':None,
			'entities':None}
		}
	return response
