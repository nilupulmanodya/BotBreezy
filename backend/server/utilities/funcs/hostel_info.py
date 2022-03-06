from flask import session
def hostel_info(utterance,mycursor,db_connection):
	try:
		#db query for hostel_info
		#print('session is :',session['ses_validate'])
		
		mycursor.execute("SELECT * FROM hostel_info") 
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
		print('hostel_info querry not success...Internal server ERROR in fun hostel_info')
		response = {'fun_res':{
			'is_completed':False,
			'content':None,
			'is_option':False,
			'is_entity':False,
			'options':None,
			'entities':None}
		}
	return response
