from flask import session
from ..entity_extractor import Entity_extractor

def faculty_info(utterance,mycursor):
	
	#updating session 
	#function consists one entity COU
	print('begining course info',session['ses_validate'])
	session['ses_validate']['entities']={
		'FAC':None,
		}	
	print("after 1 update",session['ses_validate'])

	
		#ent_PLA        
	ent_FAC=str()
	ent_FAC_ls=[]
	entities = Entity_extractor(utterance)
	
	
	if len(entities)>0:
		for i in range(0, len(entities)):

			#entities needs to course_info (bio medical engineering,computer science)
			if entities[i]['ent_data'][2]=='FAC':
				ent_FAC = entities[i]['ent_data'][0]
				ent_FAC_ls.append(entities[i])
				
				#print(ent_COU_ls)
				#pint('COU entity detected')
		if len(ent_FAC_ls)==1:
			if ent_FAC == 'foe':
				#session update for entity
				session['ses_validate']['entities']={
				'FAC':'foe'
				}	
				#db query for faculty info (foe)..
				mycursor.execute("SELECT * FROM faculty_info WHERE fac_lbl_name='foe'")
				myresult = mycursor.fetchall()
				
				
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'FAC'}
							}
				return response

			elif ent_FAC == 'foc':
				#session update for entity
				session['ses_validate']['entities']={
				'FAC':'foc'
				}
				
				#db query for faculty info (foc)..
				
				mycursor.execute("SELECT * FROM faculty_info WHERE fac_lbl_name='foc'")
				myresult = mycursor.fetchall()
				response = {'fun_res':{
					'is_completed':True,
					'content':myresult[0][1],
					'is_option':False,
					'is_entity':False,
					'options':None,
					'entities':'FAC'}}
				return response
		else:
			response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me, which faculty information do you need ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Faculty of Engineering','Faculty of Computing']}}
			#return to choose intent
			session['ses_validate']['understand']-=1
			return response
			
			
	if (ent_FAC==''):
		#no entity found
		#return to choose intent
		response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me, which faculty information do you need ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Faculty of Engineering','Faculty of Computing']}}
		#two options
		session['ses_validate']['understand']-=1
		print(session['ses_validate']['understand'])
		return response
		
		 
