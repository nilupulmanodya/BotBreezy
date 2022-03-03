from flask import session
from ..entity_extractor import Entity_extractor

def sports_info(utterance,mycursor):
	print("entered")
	#updating session 
	#function consists one entity COU
	print('begining sports info',session['ses_validate'])
	session['ses_validate']['entities']={
		'SPT':None,
		}	
	print("after 1 update",session['ses_validate'])

	
		#ent_SPT
	ent_SPT=str()
	ent_SPT_ls=[]
	entities = Entity_extractor(utterance)
	
	
	if len(entities)>0:
		for i in range(0, len(entities)):

			#entities needs to SPT_info (karate,cricket)
			if entities[i]['ent_data'][2]=='SPT':
				ent_SPT = entities[i]['ent_data'][0]
				ent_SPT_ls.append(entities[i])
				
				#print(ent_COU_ls)
				#pint('COU entity detected')
		if len(ent_SPT_ls)==1:
			if ent_SPT == 'krt':
				#session update for entity
				session['ses_validate']['entities']={
				'SPT':'krt'
				}	
				#db query for course info (cbme)..
				mycursor.execute("SELECT * FROM sports_info WHERE sport_name ='krt'")
				myresult = mycursor.fetchall()
				
				
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'SPT'}
							}
				return response

			elif ent_SPT == 'cri':
				#session update for entity
				session['ses_validate']['entities']={
				'SPT':'cri'
				}
				
				#db query for course info (ccs)..
				
				mycursor.execute("SELECT * FROM sports_info WHERE sport_name ='cri'")
				myresult = mycursor.fetchall()
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'SPT'}}
				return response
		else:
			response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me which sport details you need ? You can choose Karate or Cricket as Demo University Student',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Karate','Cricket']}}
			#return to choose intent
			session['ses_validate']['understand']-=1
			return response
			
			
	if (ent_SPT==''):
		#no entity found
		#return to choose intent
		response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me which sport details you need ? You can choose Karate or Cricket as Demo University Student',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Karate','Cricket']}}
		#two options
		session['ses_validate']['understand']-=1
		print(session['ses_validate']['understand'])
		return response
		
		 
