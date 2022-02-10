from flask import session
from ..entity_extractor import Entity_extractor

def reg_event(utterance,mycursor):
	
	#updating session 
	#function consists one entity EVT
    if session['ses_validate']['entities']==None:
        print('begining reg event',session['ses_validate'])
        session['ses_validate']['entities']={
            'EVT':None,'PSL':None
            }
        print("after 1 update",session['ses_validate'])
    #session['ses_validate']['entities']={'EVT':None}
    print('..................',session['ses_validate'])
	
	#ent_PLA        
    ent_EVT=str()
    ent_EVT_ls=[]
    ent_PSL=str()
    ent_PSL_ls=[]
    entities = Entity_extractor(utterance)
    
    if session['ses_validate']['entities']['EVT']==None:
      #print('getting to the evt')
      if len(entities)>0:
          for i in range(0, len(entities)):
            #print('getting to for loop')

                #entities needs to reg_event:events (robotic day, invention day)
            if entities[i]['ent_data'][2]=='EVT':
              ent_EVT = entities[i]['ent_data'][0]
              ent_EVT_ls.append(entities[i])

              #print(ent_EVT_ls)
              print('EVT entity detected')
          if len(ent_EVT_ls)==1:
                if ent_EVT == 'rbd':
                    #session update for entity
                    session['ses_validate']['entities']['EVT']='rbd'
                   
                elif ent_EVT == 'ine':
                    #session update for entity
                    session['ses_validate']['entities']['EVT']='ine'

                    
          else:
                response = {'fun_res':{
                        'is_completed':False,
                        'content':'Tell me, which event do you like to register ?',
                        'is_option':False,
                        'is_entity':True,
                        'options':None,
                        'entities':['Robotics Day','Invention Exhibition']}}
                #return to choose intent
                session['ses_validate']['understand']-=1
                return response
            
    if session['ses_validate']['entities']['PSL']==None:
        if len(entities)>0:
            for i in range(0, len(entities)):

                #entities needs to reg_event:reg num (S***)
                if entities[i]['ent_data'][2]=='PSL':
                    ent_PSL = entities[i]['ent_data'][0]
                    ent_PSL_ls.append(entities[i])

                    #print(ent_PSL_ls)
                    #pint('EVT ent_PSL detected')
            if len(ent_PSL_ls)==1:
                if ent_PSL == 'rg':
                    #session update for entity
                    session['ses_validate']['entities']['PSL']=ent_PSL_ls[0]['ent_data'][1]                   
            else:
                print('8989898989',session['ses_validate'])
                response = {'fun_res':{
                        'is_completed':False,
                        'content':'Tell me your student registration number ?',
                        'is_option':False,
                        'is_entity':True,
                        'options':None,
                        'entities':None}}
                #return to choose intent
                session['ses_validate']['understand']-=1
                return response
        
    if session['ses_validate']['entities']['PSL'] !=None and session['ses_validate']['entities']['EVT']!=None:
        
        #checking the registered evt
        if session['ses_validate']['entities']['EVT']=='ine':
        #function success
        
            #db query

            #API calling

            #generating and return response with successs status
            response = {'fun_res':{
                        'is_completed':True,
                        'content':'Okay.. Successfully registered '+session['ses_validate']['entities']['PSL']+' to Invention Exhibition',
                        'is_option':False,
                        'is_entity':False,
                        'options':None,
                        'entities':['EVT','PSL']}}
            return response
        
        elif session['ses_validate']['entities']['EVT']=='rbd':
            #function success
        
            #db query

            #API calling

            #generating and return response with successs status
            response = {'fun_res':{
                        'is_completed':True,
                        'content':'Okay.. Successfully registered '+session['ses_validate']['entities']['PSL']+' to Robotics Day',
                        'is_option':False,
                        'is_entity':False,
                        'options':None,
                        'entities':['EVT','PSL']}}
            return response
        else:
            print('Error occured event_reg')
    if (ent_EVT==''):
		#no entity found
		#return to choose intent
        response = {'fun_res':{
					'is_completed':False,
					'content':'Tell me, which event do you like to register ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Robotics Day','Invention Exhibition']}}
		#two options
        session['ses_validate']['understand']-=1
        print(session['ses_validate']['understand'])
        return response
		
		 
