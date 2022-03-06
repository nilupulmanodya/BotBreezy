from flask import session
from ..entity_extractor import Entity_extractor

def course_info(utterance,mycursor,db_connection):
	
	#updating session 
	#function consists one entity COU
	print('begining course info',session['ses_validate'])
	session['ses_validate']['entities']={
		'COU':None,
		}	
	print("after 1 update",session['ses_validate'])

	
		#ent_PLA        
	ent_COU=str()
	ent_COU_ls=[]
	entities = Entity_extractor(utterance)
	
	
	if len(entities)>0:
		for i in range(0, len(entities)):

			#entities needs to course_info (bio medical engineering,computer science)
			if entities[i]['ent_data'][2]=='COU':
				ent_COU = entities[i]['ent_data'][0]
				ent_COU_ls.append(entities[i])
				
				#print(ent_COU_ls)
				#pint('COU entity detected')
		if len(ent_COU_ls)==1:
			if ent_COU == 'cbme':
				#session update for entity
				session['ses_validate']['entities']={
				'COU':'bme'
				}	
				#db query for course info (cbme)..
				mycursor.execute("SELECT * FROM course_info WHERE course_name ='bme'")
				myresult = mycursor.fetchall()
				
				
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'COU'}
							}
				return response

			elif ent_COU == 'ccs':
				#session update for entity
				session['ses_validate']['entities']={
				'COU':'bme'
				}
				
				#db query for course info (ccs)..
				
				mycursor.execute("SELECT * FROM course_info WHERE course_name ='cs'")
				myresult = mycursor.fetchall()
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'COU'}}
				return response
		else:
			response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me which course ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Computer Science','Bio Medical Engineering']}}
			#return to choose intent
			session['ses_validate']['understand']-=1
			return response
			
			
	if (ent_COU==''):
		#no entity found
		#return to choose intent
		response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me which course ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Computer Science','Bio Medical Engineering']}}
		#two options
		session['ses_validate']['understand']-=1
		print(session['ses_validate']['understand'])
		return response
		
		 
