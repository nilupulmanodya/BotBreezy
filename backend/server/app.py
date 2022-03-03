from flask import Flask, request, session
from utilities.intent_validation import *
from utilities import db_connection,dispatcher,entity_extractor

app=Flask(__name__)



#this function only for testing purposes
@app.route("/test")
def test():
	grs()
	print(session['ses_validate'])
	print(session['ses_validate']['understand'])
	return "<p>test url</p>"


@app.route("/botbreezy",methods=['POST','GET'])
def chatbot():
	if not session:
		print("session unavailable")
		grs()
	
	
	
	s=session['ses_validate']
	print(session['ses_validate'])
	#check weather understand is less than 0 or not
	if s['understand']<1:
		
		response = {'fun_res':{
					'is_completed':False,
					'content':"Sorry I can't understand",
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':None}}
		print(session['ses_validate'])
		
		grs()
		#print(session['ses_validate'])
		return response
	
	#if understand is >0
	else:
		
		if request.method == 'POST':
			body=request.json
			print(request)
			print('body is:',body)
			if body['utterance']:		
				print(body['utterance'])
				
				#check weather intent already exists or not
				if not session['ses_validate']['func_available']:
					top_classes = Validate_top_class(Intent_clasification(body['utterance']))
					if top_classes['validated_top_class']==True:
						#calling function
						print('top class found.. top class is>>: ',top_classes['top_class'])
						res_func=call_func(top_classes['top_class'],body['utterance'],None)
						#print(res_func)
						#check weather function is completed or not
						print('resssss is******',res_func)
						if res_func['fun_res']['is_completed']==True:
							print('function successfully completed')
							grs()
							return res_func
							
						else:
							print("function still not completed...may be entities required")
							return res_func
					else:
						#suggesting top 3 classes to user
						print('suggest top three classes')
				else:
					#calling exists func with input utterance
					print('calling exisiting funcs')
					res_func=call_func(session['ses_validate']['func'],body['utterance'],session['ses_validate']['entities'])
						
					#check weather function is completed or not
					if res_func['fun_res']['is_completed']==True:
						print('function successfully completed')
						grs()
						return res_func
						
					else:
						print("function still not completed...may be entities required")
						return res_func
			else:
				print('no utterance found in body')		
			print('post method form validated')
		else:	
			print("no input data found")
		#need to develop return	
		return "no input data found"

	
#generated response / default session
def grs(uncertainty=None,func=None,entities=None,understand=4,func_available=False):
	session['ses_validate']={
		'uncertainty':uncertainty,
		'func':func,
		'entities':entities,
		'understand':understand,
		'func_available':func_available}
	print('initial session created success')

	return 0


#calling functions through dispatcher
def call_func(func,utterance,entities):	
	try:
		print("func iss",func)
		#print(db_connection.mydb)
		grs(uncertainty=None,func=func,entities=entities,understand=session['ses_validate']['understand'],func_available=True)#updating session for funcion
		fun_res = dispatcher.dispatcher[func](utterance,db_connection.mycursor,db_connection.mydb)
		print(session['ses_validate'])
		return fun_res
	except:
		return "Invalid function"


if __name__ =="__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'

	
	app.debug = True
	app.run()
	

