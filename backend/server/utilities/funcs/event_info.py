from flask import session
from ..entity_extractor import Entity_extractor

def event_info(utterance,mycursor,db_connection):
	
	#updating session 
	#function consists one entity EVT
	print('begining course info',session['ses_validate'])
	session['ses_validate']['entities']={
		'EVT':None,
		}	
	print("after 1 update",session['ses_validate'])

	
		#ent_PLA        
	ent_EVT=str()
	ent_EVT_ls=[]
	entities = Entity_extractor(utterance)
	
	
	if len(entities)>0:
		for i in range(0, len(entities)):

			#entities needs to event_info (robotic day, invention day)
			if entities[i]['ent_data'][2]=='EVT':
				ent_EVT = entities[i]['ent_data'][0]
				ent_EVT_ls.append(entities[i])
				
				#print(ent_EVT_ls)
				#pint('EVT entity detected')
		if len(ent_EVT_ls)==1:
			if ent_EVT == 'rbd':
				#session update for entity
				session['ses_validate']['entities']={
				'EVT':'rbd'
				}	
				#db query for event info ('rbd')..
				mycursor.execute("SELECT * FROM event_info WHERE event_label ='rbd'")
				myresult = mycursor.fetchall()
				
				
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'EVT'}
							}
				return response

			elif ent_EVT == 'ine':
				#session update for entity
				session['ses_validate']['entities']={
				'EVT':'ine'
				}
				
				#db query for event info (ine)..
				
				mycursor.execute("SELECT * FROM event_info WHERE event_label ='ine'")
				myresult = mycursor.fetchall()
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'EVT'}}
				return response
		else:
			response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me, which event information do you need ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Robotics Day','Invention Exhibition']}}
			#return to choose intent
			session['ses_validate']['understand']-=1
			return response
			
			
	if (ent_EVT==''):
		#no entity found
		#return to choose intent
		response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me, which event information do you need ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Robotics Day','Invention Exhibition']}}
		#two options
		session['ses_validate']['understand']-=1
		print(session['ses_validate']['understand'])
		return response
		
		 
